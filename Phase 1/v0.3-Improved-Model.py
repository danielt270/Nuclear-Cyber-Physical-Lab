"""
============================================================================================================
PHASE 1 — v0.3
IMPROVED MODEL
============================================================================================================
OVERVIEW: 
    Improves the physical model by introducing more realistic fluid properties and heat losses. The goal is to move beyond the idealized tank model while keeping the system simple enough to understand and validate.

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
    Transient Energy Balance (Eqn. 1):
        dE/dt = Q̇_heater - Q̇_loss + ṁ(h_in - h_out)

    Heat Loss (Eqn. 2):
        Q̇_loss = U * A(T - T_surr)

    Fluid Properties (Eqn. 3):
        h = h(T,P)
        u = u(T,P)

    Numerical Integration (Eqn. 4):
        U_(n+1) = U_n + dU/dt * dt
    
    Specific Internal Energy (Eqn. 5):
        u = U/m

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
TANK_AREA          = 1        # m²
U_COEFF            = 10       # W/(m²·K) - Overall heat transfer coefficient

# Inputs
surrTemp       = float(input("Enter the surrounding temperature (°C): "))
initialTemp    = float(input("Enter the initial temperature of the water in the tank (°C): "))
inletTemp      = float(input("Enter the inlet temperature of the coolant (°C): "))
tankMass       = float(input("Enter the mass of water in the tank (kg): "))
massFlowRate   = float(input("Enter the mass flow rate of the coolant (kg/s): "))
heaterPower    = float(input("Enter the heater power (W): "))
simulationTime = float(input("Enter the total simulation time (s): "))
timeStep       = float(input("Enter the simulation timestep (s): "))

def main():
    # Calculate the number of simulation steps
    numSteps = int(simulationTime / timeStep)

    # Initialize tank temperature
    tankTemp = initialTemp  

    # Get inlet specific enthalpy (h_i)
    inletEnthalpy = CP.PropsSI('H', 'T', inletTemp + 273.15, 'P', PRESSURE, FLUID)  # J/kg

    # Get initial specific internal energy
    internalEnergy = CP.PropsSI('U', 'T', tankTemp + 273.15, 'P', PRESSURE, FLUID)  # J/kg

    # Calculate total internal energy stored in the tank
    tankEnergy = tankMass * internalEnergy

    # Calculate the temperature at each timestep
    for i in range(numSteps + 1):
        # Get fluid properties at the current tank temperature (Eqn. 3)
        enthalpy = CP.PropsSI('H', 'T', tankTemp + 273.15, 'P', PRESSURE, FLUID)  # J/kg
        internalEnergy = CP.PropsSI('U', 'T', tankTemp + 273.15, 'P', PRESSURE,FLUID)  # J/kg

        # Calculate heat loss to the surroundings (Eqn. 2)
        heatLoss = U_COEFF * TANK_AREA * (tankTemp - surrTemp) # W

        # Calculate the rate of energy entering/leaving the tank (Eqn. 1)
        energyRate = heaterPower - heatLoss + massFlowRate * (inletEnthalpy - enthalpy) # W

        print(f"\nTime: {i * timeStep:.2f} s")
        print(f"Enthalpy: {enthalpy:.2f} J/kg")
        print(f"Internal Energy: {internalEnergy:.2f} J/kg")
        print(f"Heat Loss: {heatLoss:.2f} W")
        print(f"Rate of Energy Change: {energyRate:.2e} W")
        print(f"Tank Temperature: {tankTemp:.2f} °C")

        # ADVANCES FROM n TO n+1 HERE
        # Update total tank energy using numerical integration (Eqn. 4)
        tankEnergy = tankEnergy + energyRate * timeStep

        # Calculate the new specific internal energy (Eqn. 5)
        internalEnergy = tankEnergy / tankMass

        # Calculate the new tank temperature from internal energy
        tankTemp = CP.PropsSI('T', 'U', internalEnergy, 'P', PRESSURE, FLUID) - 273.15

if __name__ == "__main__":
    main()
