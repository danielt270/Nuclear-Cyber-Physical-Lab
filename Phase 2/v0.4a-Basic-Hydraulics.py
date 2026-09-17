"""
============================================================================================================
PHASE 2 — v0.4a
BASIC HYDRAULICS
============================================================================================================
OVERVIEW: 
    The goal is to determine how flow rate, pipe geometry, fluid properties, and friction affect the pressure of a pipe system. Major losses are included with minor losses neglected.

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
        ΔP = f (L/D) (ρ * v² / 2)

    Laminar Friction Factor (Eqn. 6):
        f = 64 / Re

    Fluid Properties (Eqn. 7):
        ρ = ρ(T,P)
        μ = μ(T,P)

    Hydraulic Power Required (Eqn. 8):
        P_hydraulic = ΔP * V̇

    Volumetric Flow Rate (Eqn. 9):
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
