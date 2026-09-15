"""
============================================================================================================
PHASE 1 — v0.2
TRANSIENT HEATED TANK
============================================================================================================
OVERVIEW: 
    Building on the steady-state heated pipe from v0.1, this model represents water stored in a well-mixed 
    tank. Water flows continuously into and out of the tank while heater power and inlet flow cause the 
    tank temperature to change over time.

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
    - constant mass flow rate
    - constant pressure
    - single-phase water
    - adiabatic

EQUATIONS:
    Transient Energy Balance:
        dT/dt(m * Cp) = Q̇ + ṁ_in * Cp * (T_in - T)

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

import CoolProp.CoolProp as CP

# Constants
PRESSURE           = 101325   # Pa
FLUID              = "Water"

# Inputs
initialTemp    = float(input("Enter the initial temperature of the water in the tank (°C): "))
tankMass       = float(input("Enter the mass of water in the tank (kg): "))
inletTemp      = float(input("Enter the inlet temperature of the coolant (°C): "))
massFlowRate   = float(input("Enter the mass flow rate of the coolant (kg/s): "))
heaterPower    = float(input("Enter the heater power (W): "))
simulationTime = float(input("Enter the total simulation time (s): "))
timeStep       = float(input("Enter the simulation timestep (s): "))

def main():
    # Calculate the number of simulation steps
    numSteps = int(simulationTime / timeStep)

    # Initialize tank temperature
    tankTemp = initialTemp  

    # Calculate the temperature at each timestep
    for i in range(1, numSteps + 1):
        # Get specific heat capacity of the fluid at the current tank temperature
        cp = CP.PropsSI('C', 'T', tankTemp + 273.15, 'P', PRESSURE, FLUID)  # J/(kg·K)

        # Calculate the rate of temperature change
        dTdt = (heaterPower + massFlowRate * cp * (inletTemp - tankTemp)) / (tankMass * cp)

        # Calculate tank temperature at the next timestep using numerical integration formula
        tankTemp = tankTemp + dTdt * timeStep

        print(f"\nSpecific Heat Capacity of Water: {cp:.2f} J/(kg·K)")
        print(f"Rate of temperature change: {dTdt:.2e} °C/s")
        print(f"Time: {i * timeStep:.2f} s, Tank Temperature: {tankTemp:.2f} °C\n")

if __name__ == "__main__":
    main()
