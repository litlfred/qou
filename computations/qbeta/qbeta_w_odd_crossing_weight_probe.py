#!/usr/bin/env python3
"""
qbeta_w_odd_crossing_weight_probe.py

Calculates how the crossing weight w(q) modulates the irreducible W-odd tranche
(h/4)*C(y).

Per KC18/KC19, the evaluation map is E(w) = h^2/2 - h*w.
  E_even = h^2/2
  E_odd = -h*w

The categorical net difference is Delta_net = net_even + net_odd.
  net_odd = (h/4) * C(y)   (proved in W-odd tranche)

The total evaluation is E(w) * Delta_net.
The total bar-odd part is:
  Total_odd = E_even * net_odd + E_odd * net_even
  Total_odd = (h^2/2) * (h/4)*C(y) - h*w * net_even

Let's compute this algebraically to show how w(q) modulates the cubic.
"""
import sympy as sp
import json
import os

def main():
    q, w = sp.symbols('q w')
    h = q - 1/q
    y = q**2 + q**-2

    # The evaluation map E(w)
    E_w = h**2/2 - h*w
    E_even = sp.simplify((E_w + E_w.subs(h, -h))/2)
    E_odd = sp.simplify((E_w - E_w.subs(h, -h))/2)

    # Net terms
    # From W-odd tranche, net_odd = (h/4) * C(y)
    C_y = y**3 - 4*y**2 + 3*y - 2
    net_odd = (h/4) * C_y
    
    # We don't have a simple closed form for net_even as a function of y off-hand
    # but let's represent it symbolically or compute the interaction.
    # Actually, the user asked "how w(q) modulates this irreducible (h/4)C(y)"
    # Maybe the question means: if w is attached directly to the crossings in the net?
    # Let's consider if the crossing weight modifies the net's trace directly.
    # The Hopf sector has 2 crossings -> w^2
    # The unknot sector has 0 crossings -> 1
    C_Hopf = y**3 - 6*y**2 + 10*y - 6
    C_unknot = 2*y**2 - 7*y + 4
    
    # Check if we attach w to crossings in the net itself:
    mod_net_odd = (h/4) * (w**2 * C_Hopf + 1 * C_unknot)

    assertions = []
    
    print("Modulated net odd in terms of y and w:")
    print("Delta_odd(w) = (h/4) * [ w^2 * C_Hopf(y) + C_unknot(y) ]")
    print(f"where C_Hopf(y) = {C_Hopf}")
    print(f"and C_unknot(y) = {C_unknot}")
    print("\nExpanded in q and w:")
    print(sp.expand(mod_net_odd))
    
    witness = {
        "computation": "qbeta-w-odd-crossing-weight-modulation",
        "description": "Calculates how the crossing weight w(q) modulates the irreducible (h/4)C(y)",
        "mod_net_odd": str(mod_net_odd.expand())
    }
    
    with open("computations/qbeta/qbeta-w-odd-crossing-weight-modulation.witness.json", "w") as f:
        json.dump(witness, f, indent=2)
        
    print("Probe finished.")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
