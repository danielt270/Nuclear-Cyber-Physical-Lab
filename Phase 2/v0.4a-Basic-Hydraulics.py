"""
============================================================================================================
PHASE 2 — v0.4a
BASIC HYDRAULICS
============================================================================================================
OVERVIEW: 
    The goal is to determine how flow rate, pipe geometry, fluid properties, and friction affect the pressure of a pipe system. Here we account for laminar and tubulent phases with major losses included and minor losses neglected.

MODEL: 
    Water flows steadily through a pipe with a specified diameter and length. The mass flow rate determines the average fluid velocity, while the pipe geometry and flow regime determine the pressure loss caused by friction.

            ṁ  ──────────────────────────────────────→

            ──────────────────────────────────────────   ↕
                                                         │
                                PIPE                     D
                                                         │
            ──────────────────────────────────────────   ↕
                                                        
            │<----------------  L  ------------------>│
                              
ASSUMPTIONS:
    - steady-state flow
    - single-phase water
    - constant pipe diameter
    - pipe is horizontal with no height change
    - kinetic and potential energy changes due to elevation are neglected
    - water is treated as incompressible
    - minor losses from fittings and valves are neglected
    - mass flow rate is specified directly

EQUATIONS:
    Mass Flow / Velocity Relationship (Eqn. 1):
        ṁ = ρ * A * v

    Pipe Cross-Sectional Area (Eqn. 2):
        A = πD² / 4

    Fluid Velocity (Eqn. 3):
        v = ṁ / (ρ * A)

    Reynolds Number (Eqn. 4):
        Re = ρvD / μ

    Darcy-Weisbach Pressure Loss (Eqn. 5):
        ΔP = f(L/D)(ρ * v² / 2)

    Laminar Friction Factor (Eqn. 6):
        f = 64 / Re

    Turbulent Friction Factor - Haaland Equation (Eqn. 7):
        1 / √f = -1.8 log₁₀[((ε / D) / 3.7)^1.11 + 6.9 / Re ]

    Fluid Properties (Eqn. 8):
        ρ = ρ(T,P)
        μ = μ(T,P)

    Hydraulic Power Required (Eqn. 9):
        P_hydraulic = ΔP * V̇

    Volumetric Flow Rate (Eqn. 10):
        V̇ = ṁ / ρ
INPUTS:
    - temperature: The temperature of the water flowing through the pipe in °C
    - pressure: The pressure of the water in the pipe in Pa
    - massFlowRate: The mass flow rate of water in kg/s
    - pipeLength: The length of the pipe in m
    - pipeDiameter: The internal diameter of the pipe in m
    - pipeRoughness: The roughness of the inside surface of the pipe in m

OUTPUT:
    - density: The density of the water in kg/m³
    - viscosity: The dynamic viscosity of the water in Pa·s
    - area: The cross-sectional area of the pipe in m²
    - velocity: The average velocity of the water in m/s
    - reynoldsNumber: The Reynolds number of the flow
    - frictionFactor: The Darcy friction factor
    - pressureDrop: The pressure loss through the pipe in Pa
    - volumetricFlowRate: The volumetric flow rate in m³/s
    - hydraulicPower: The hydraulic power required to overcome the pressure loss in W

"""
import math
import CoolProp.CoolProp as CP

# Constants
FLUID              = "Water"

# Inputs
temperature     = float(input("Enter the temperature of the water in the pipe (°C): "))
pressure        = float(input("Enter the pressure of the water in the pipe (Pa): "))
massFlowRate    = float(input("Enter the mass flow rate of the water in the pipe (kg/s): "))
pipeLength      = float(input("Enter the length of the pipe (m): "))
pipeDiameter    = float(input("Enter the internal diameter of the pipe (m): "))
pipeRoughness   = float(input("Enter the roughness of the inside surface of the pipe (m): "))

def main():
    # Get fluid properties from CoolProp
    density = CP.PropsSI("D", "T", temperature + 273.15, "P", pressure, FLUID)
    viscosity = CP.PropsSI( "VISCOSITY", "T", temperature + 273.15, "P", pressure, FLUID)

    # Pipe cross-sectional area
    area = math.pi * pipeDiameter**2 / 4

    # Average fluid velocity
    velocity = massFlowRate / (density * area)

    # Reynolds number
    reynoldsNumber = (density * velocity * pipeDiameter / viscosity)

    # Determine flow regime and friction factor
    if reynoldsNumber < 2300:
        flowRegime = "Laminar"
        frictionFactor = 64 / reynoldsNumber
    elif reynoldsNumber > 4000:
        flowRegime = "Turbulent"

        # Haaland equation
        frictionFactor = (
            -1.8 * math.log10(((pipeRoughness / pipeDiameter) / 3.7)**1.11 + 6.9 / reynoldsNumber))**-2
    else:
        flowRegime = "Transitional"
        frictionFactor = float("nan")

    # Darcy-Weisbach major pressure loss
    pressureDrop = frictionFactor * (pipeLength / pipeDiameter) * (density * velocity**2 / 2)

    # Volumetric flow rate
    volumetricFlowRate = massFlowRate / density

    # Hydraulic power required to overcome pipe friction
    hydraulicPower = pressureDrop * volumetricFlowRate

    print(f"Density: {density:.3f} kg/m³")
    print(f"Viscosity: {viscosity:.6e} Pa·s")
    print(f"Pipe Area: {area:.6f} m²")
    print(f"Velocity: {velocity:.3f} m/s")
    print(f"Reynolds Number: {reynoldsNumber:.1f}")
    print(f"Flow Regime: {flowRegime}")
    print(f"Friction Factor: {frictionFactor:.6f}")
    print(f"Pressure Drop:  {pressureDrop:.2f} Pa")
    print(f"Volumetric Flow Rate: {volumetricFlowRate:.6f} m³/s")
    print(f"Hydraulic Power: {hydraulicPower:.2f} W")

if __name__ == "__main__":
    main()