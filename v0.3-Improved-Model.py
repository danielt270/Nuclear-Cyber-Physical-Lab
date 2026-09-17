"""
============================================================================================================
PHASE 1 — v0.3
IMPROVED MODEL
============================================================================================================
OVERVIEW: 
    Improves the physical model by introducing more realistic fluid properties, pressure, heat losses, and 
    physical limits. The goal is to move beyond the idealized tank model while keeping the system simple 
    enough to understand and validate.

MODEL: 
    Water is stored in a well-mixed heated tank and flows continuously through the system. The tank 
    temperature changes over time based on the energy added by the heater, energy carried into and out of 
    the tank by the coolant flow, and heat lost due to surroundings.

                            Heater
                              Q̇
                              ↓
                     ┌─────────────────┐
                     │                 │
          ṁ_in →  ───┘      WATER      └─── → ṁ_out
          T_in    ───┐       T(t)      ┌───  T_out
                     │                 │
                     └────────┬────────┘
                              │
                         Surroundings
                           Heat Loss
                            Q̇_loss
                              ↓
                         
                            where    
                         ṁ_in = ṁ_out
                              
ASSUMPTIONS:
    - tank is well-mixed
    - transient state
    - constant tank mass
    - constant mass flow rate
    - single-phase water
    - kinetic and potential energy changes are negligible

EQUATIONS:
    Transient Energy Balance:
        dE/dt = Q̇_heater - Q̇_loss + ṁ(h_in - h_out)

    Heat Loss:
        Q̇_loss = U * A(T - T_surr)

    Fluid Properties:
        h = h(T,P)
        u = u(T,P)
        ρ = ρ(T,P)
        Cp = Cp(T,P)

    Numerical Integration:
        T_(n+1) = T_n + dT/dt * dt

INPUTS:
    - initialTemp: The initial temperature of water in the tank in °C
    - tankMass: The mass of water contained in the tank in kg
    - inletTemp: The inlet temperature of water in °C
    - massFlowRate: The mass flow rate of water in kg/s
    - heaterPower: The power supplied by the heater in W
    - surrTemp: The surrounding temperature in °C
    - simulationTime: The total simulation time in seconds
    - timeStep: The simulation timestep in seconds

OUTPUT:
    - tankTemp: The temperature of the water in the tank as a function of time
    - heatLoss: The rate of heat lost from the tank as a function of time
    - enthalpy: The specific enthalpy of the water as a function of time
    - internalEnergy: The specific internal energy of the water as a function of time
    - density: The density of the water as a function of time
    - cp: The specific heat capacity of the water as a function of time
    - pressure: The pressure of the water in the tank
"""

import CoolProp.CoolProp as CP

# Constants
PRESSURE           = 101325   # Pa
FLUID              = "Water"
TANK_AREA          = 1.0      # m²
U_COEFF            = 1.0      # W/(m²·K) - Overall heat transfer coefficient

# Inputs
initialTemp    = float(input("Enter the initial temperature of the water in the tank (°C): "))
tankMass       = float(input("Enter the mass of water in the tank (kg): "))
inletTemp      = float(input("Enter the inlet temperature of the coolant (°C): "))
massFlowRate   = float(input("Enter the mass flow rate of the coolant (kg/s): "))
heaterPower    = float(input("Enter the heater power (W): "))
surrTemp       = float(input("Enter the surrounding temperature in °C: "))
simulationTime = float(input("Enter the total simulation time (s): "))
timeStep       = float(input("Enter the simulation timestep (s): "))

def main():





if __name__ == "__main__":
    main()
