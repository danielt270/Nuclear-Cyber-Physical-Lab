"""
============================================================================================================
PHASE 1 — v0.1
STEADY-STATE HEATED PIPE
============================================================================================================
OVERVIEW: 
    Starting with a simple steady-state heated pipe, this model calculates the outlet temperature of 
    continuously flowing water based on its inlet temperature, mass flow rate, and applied heater power. 
    The model will then be expanded into a transient tank, introducing stored mass and temperature changes.

MODEL: 
    Water flows continuously through a heated section

                               Heater
                                 Q̇ 
                                 │
                                 │
                  ───────────────▼───────────────
                                               
        ṁ_in ───→              WATER              ───→ ṁ_out
        T_in                                           T_out
                  ───────────────────────────────
                               where    
                            ṁ_in = ṁ_out
    
ASSUMPTIONS:
    - steady state
    - constant pressure
    - adiabatic
    - constant mass flow rate
    - constant fluid properties
    - single-phase water
    - kinetic and potential energy changes are negligible
                         
EQUATIONS:
    Specific heat equation:
        Q = m_dot * Cp(T_out - T_in)                  

INPUTS:
    - inletTemp: The inlet temperature of water in °C
    - massFlowRate: The mass flow rate of water in kg/s
    - heaterPower: The power of the heater in W

OUTPUTS:
    - outletTemp: The temperature of the coolant after passing through the heater and cooler.
    - cp: The specific heat capacity of the water as a function of time
============================================================================================================
"""

import CoolProp.CoolProp as CP

# Constants
PRESSURE           = 101325   # Pa
FLUID              = "Water"

# Inputs
inletTemp    = float(input("Enter the inlet temperature of the coolant (°C): "))
massFlowRate = float(input("Enter the mass flow rate of the coolant (kg/s): "))
heaterPower  = float(input("Enter the heater power (W): "))

def main():
    # Get specific heat capacity of the fluid at the inlet temperature
    cp = CP.PropsSI('C', 'T', inletTemp + 273.15, 'P', PRESSURE, FLUID)  # J/(kg·K)

    # Calculate the temperature rise using the specific heat equation
    deltaT = heaterPower / (massFlowRate * cp)

    # Calculate the outlet temperature using the specific heat equation
    outletTemp = inletTemp + deltaT

    # Outputs
    print(f"\nSpecific Heat Capacity of Water: {cp:.2f} J/(kg·K)")
    print(f"Outlet Temperature: {outletTemp:.2f} °C")

if __name__ == "__main__":
    main()













