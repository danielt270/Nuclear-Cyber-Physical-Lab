"""
============================================================================================================
PHASE 1 — v0.2
TRANSIENT HEATED TANK
============================================================================================================
OVERVIEW: 
    Starting with a simple steady-state heated pipe, this model calculates the outlet temperature of 
    continuously flowing water based on its inlet temperature, mass flow rate, and applied heater power. 
    The model will then be expanded into a transient tank, introducing stored mass and temperature changes.

MODEL: Water is stored and flows continuously through a well-mixed heated tank, with its temperature changing over time.

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
    - steady flow





"""
