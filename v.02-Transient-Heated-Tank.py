"""
============================================================================================================
PHASE 1 — v0.2
TRANSIENT HEATED TANK
============================================================================================================
OVERVIEW: 
    Starting with a simple steady-state heated pipe, this model calculates the outlet temperature of 
    continuously flowing water based on its inlet temperature, mass flow rate, and applied heater power. 
    The model will then be expanded into a transient tank, introducing stored mass and temperature changes.

MODEL: 
    Water is stored and flows continuously through a well-mixed heated tank, with its temperature 
    changing over time.

                  Heater
                    Q̇
                    ↓
              ┌─────────────┐
              │             │
      ṁ_in →  │    WATER    │ → ṁ_out
      T_in    │     T(t)    │   T_out
              │             │
              └─────────────┘
                   where    
                ṁ_in = ṁ_out

ASSUMPTIONS:
    - tank is well-mixed
    - transient state
    - constant tank mass
    - constant pressure
    - single phase water
    - adiabatic

EQUATIONS:
    Transient Energy Balance:
        dT/dt = (Q̇ + ṁ_in * Cp * (T_in - T)) / (m * Cp)

    Numerical Integration:
        T_(n+1) = T_n + dT/dt * dt

INPUTS:
    - initialTemp: The initial temperature of water in the tank in °C
    - tankMass: The mass of water contained in the tank in kg
    - inletTemp: The inlet temperature of water in °C
    - massFlowRate: The mass flow rate of water in kg/s
    - heaterPower: The power of the heater in W
    - simulationTime: The total simulation time in seconds
    - timeStep: The simulation timestep in seconds

OUTPUT:
    - tankTemp: The temperature of the water in the tank as a function of time
"""
