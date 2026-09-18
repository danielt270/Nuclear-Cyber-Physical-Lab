"""
============================================================================================================
PHASE 2 — v0.4b
PUMP-INDUCED FLOW
============================================================================================================
OVERVIEW: 
    Improving upon v0.4a, a pump now dictates the flow instead of a specified constant mass flow rate. The goal is to determine determines the steady-state operating point between the pump pressure rise and the pressure loss of the pipe.

MODEL: 


                            PUMP
                       ┌───────────────┐
                       │               │
                       │  Pump Curve   │
                       │               │
                       └───────┬───────┘
                               │
                               │  Flow
                               ↓
          ──────────────────────────────────────────────
                                                        
                               PIPE                     
                                                        
          ──────────────────────────────────────────────
                               │
                               └─────────────────────────┐
                                                         │
                                                         └──→ PUMP


                         Pump Pressure Rise
                                  │
                                  │
                                  X  ← Operating Point
                                  │
                                  │
                         Pipe Pressure Loss
                                  │
                                  └──────────────────────→ Flow

                                    where
                    ΔP_pump = pressure rise produced by the pump
                    ΔP_pipe = pressure loss through the pipe
                    ṁ       = resulting mass flow rate
                    V̇       = resulting volumetric flow rate

                         At the operating point:
                            ΔP_pump = ΔP_pipe  

ASSUMPTIONS:
    - steady-state flow
    - single-phase water
    - constant pipe diameter
    - no elevation change along the pipe
    - water is treated as incompressible
    - minor losses from fittings and valves are neglected
    - mass flow rate is specified directly

EQUATIONS:
    Pump Curve (Eqn. 1):
        ΔP_pump = ΔP_shutoff - K_pump * V̇²

    Mass Flow / Volumetric Flow Relationship (Eqn. 2):
        ṁ = ρ * V̇

    Pipe Cross-Sectional Area (Eqn. 3):
        A = πD² / 4

    AverageFluid Velocity (Eqn. 4):
        v = V̇ / A

    Reynolds Number (Eqn. 5):
        Re = ρ * v * D / μ

    Laminar Friction Factor (Eqn. 6):
        f = 64 / Re

    Turbulent Friction Factor — Haaland Equation (Eqn. 7):
        1/√f = -1.8 log₁₀ [((ε / D) / 3.7)^1.11 + 6.9 / Re]

    Darcy-Weisbach Pressure Loss (Eqn. 8):
        ΔP_pipe = f (L / D) (ρ * v² / 2)

    Operating Point Condition (Eqn. 9):
        ΔP_pump = ΔP_pipe

    Volumetric Flow Rate (Eqn. 10):
        V̇ = ṁ / ρ

    Hydraulic Power (Eqn. 11):
        P_hydraulic = ΔP_pipe * V̇
INPUTS:
    - temperature: The temperature of the water in °C
    - pressure: The pressure of the water in Pa
    - pipeLength: The length of the pipe in m
    - pipeDiameter: The internal diameter of the pipe in m
    - pipeRoughness: The roughness of the inside surface of the pipe in m
    - pumpShutoffPressure: The pump pressure rise at zero flow in Pa
    - pumpCurveCoefficient: The pump curve coefficient

OUTPUT:
    - density: The density of the water in kg/m³
    - viscosity: The dynamic viscosity of the water in Pa·s
    - area: The cross-sectional area of the pipe in m²
    - volumetricFlowRate: The operating volumetric flow rate in m³/s
    - massFlowRate: The operating mass flow rate in kg/s
    - velocity: The average velocity of the water in m/s
    - reynoldsNumber: The Reynolds number of the flow
    - flowRegime: The flow regime
    - frictionFactor: The Darcy friction factor
    - pumpPressureRise: The pressure rise produced by the pump in Pa
    - pressureDrop: The pressure loss through the pipe in Pa
    - hydraulicPower: The hydraulic power delivered to the flow in W
"""
import math
import CoolProp.CoolProp as CP

# Constants
FLUID                  = "Water"
PUMP_SHUTOFF_PRESSURE  = 100000       # Pa
PUMP_CURVE_COEFFICIENT = 20_000_000  # Pa / (m^3/s)^2

# Inputs
temperature   = float(input("Enter the temperature of the water in the pipe (°C): "))
pressure      = float(input("Enter the pressure of the water in the pipe (Pa): "))
pipeLength    = float(input("Enter the length of the pipe (m): "))
pipeDiameter  = float(input("Enter the internal diameter of the pipe (m): "))
pipeRoughness = float(input("Enter the roughness of the inside surface of the pipe (m): "))

# Determines flow regime and friction factor
def calculate_friction_factor(reynoldsNumber):
    if reynoldsNumber < 2300:
        flowRegime = "Laminar"

        # Friction factor for laminar flow (Eqn. 6)
        frictionFactor = 64 / reynoldsNumber
    elif reynoldsNumber > 4000:
        flowRegime = "Turbulent"

        # Haaland equation (Eqn. 7)
        frictionFactor = (
            -1.8 * math.log10(((pipeRoughness / pipeDiameter) / 3.7)**1.11 + 6.9 / reynoldsNumber))**-2
    else:
        flowRegime = "Transitional"
        frictionFactor = None

    return flowRegime, frictionFactor

# Calculates the pressure loss through the pipe for a given volumetric flow rate
def calculate_pipe_pressure_drop(volumetricFlowRate, density, viscosity):
    # Pipe cross-sectional area (Eqn. 3)
    area = math.pi * pipeDiameter**2 / 4

    # Average fluid velocity (Eqn. 4)
    velocity = volumetricFlowRate / area

    # Reynolds number (Eqn. 5)
    reynoldsNumber = (density * velocity * pipeDiameter / viscosity)

    flowRegime, frictionFactor = calculate_friction_factor(reynoldsNumber)

    if frictionFactor is None:
        return None

    # Darcy-Weisbach Pressure Loss (Eqn. 8)
    pressureDrop = frictionFactor * (pipeLength / pipeDiameter) * (density * velocity**2 / 2)

    return pressureDrop

# Calculates the pressure rise produced by the pump for a given volumetric flow rate
def calculate_pump_pressure(volumetricFlowRate):
    # Pump Curve (Eqn. 1)
    return (PUMP_SHUTOFF_PRESSURE - PUMP_CURVE_COEFFICIENT * volumetricFlowRate**2)

# Finds the operating point where the pump pressure rise equals the pipe pressure loss
def find_operating_point(density, viscosity):
    # Starting with zero flow.
    lowerFlow = 0.0

    # At zero flow, pump pressure is at its maximum (equal to PUMP_SHUTOFF_PRESSURE)
    lowerDifference = calculate_pump_pressure(lowerFlow)

    # Estimate an upper flow limit where the pump pressure reaches zero.
    upperFlow = math.sqrt(PUMP_SHUTOFF_PRESSURE / PUMP_CURVE_COEFFICIENT)

    for _ in range(100):
        # Select the midpoint between the lower and upper flow limits
        middleFlow = (lowerFlow + upperFlow) / 2

        # Get the pump pressure (y-value) from the pump/pipe curves at the current flow rate (x-value)
        pumpPressure = calculate_pump_pressure(middleFlow)
        pipePressure = calculate_pipe_pressure_drop(middleFlow, density, viscosity)

        # Transitional flow is not modeled yet
        if pipePressure is None:
            return None

        # Compare the two pressures to determine if the operating point has been reached
        difference = pumpPressure - pipePressure

        # The operating point is where pump pressure = pipe pressure
        if abs(difference) < 0.01:
            return middleFlow

        # Pump pressure is greater, so the operating point is at a higher flow rate
        if difference > 0:
            lowerFlow = middleFlow
        # Pump pressure is less, so the operating point is at a lower flow rate
        else:
            upperFlow = middleFlow

    return middleFlow

def main():


if __name__ == "__main__":
    main()