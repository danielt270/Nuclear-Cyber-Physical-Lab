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

    Fluid Velocity (Eqn. 4):
        v = ṁ / (ρ *A)

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
FLUID              = "Water"
PUMP_SHUTOFF_PRESSURE = 100000  # Pa

# Inputs


def main():
    

if __name__ == "__main__":
    main()