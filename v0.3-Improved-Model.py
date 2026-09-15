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
    - pressure: The pressure of the water in Pa
    - inletTemp: The inlet temperature of water in °C
    - massFlowRate: The mass flow rate of water in kg/s
    - heaterPower: The power supplied by the heater in W
    - ambientTemp: The ambient temperature surrounding the tank in °C
    - U: The overall heat transfer coefficient between the tank and surroundings in W/(m²·K)
    - tankArea: The surface area of the tank exposed to the surroundings in m²
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