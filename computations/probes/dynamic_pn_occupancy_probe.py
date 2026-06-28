#!/usr/bin/env python3
"""
Probe: Dynamic p-n occupancy beyond the static Z·N graph.
Evaluates the fractional occupancy weights needed to match AME, given the
owner-gated s5-so3 keystone W_lambda representations, addressing halo-D and magic-alpha.
"""
import mpmath as mp

# E0 universal scale factor (MeV)
E0 = mp.mpf('4.2045') # Approximated from existing context, usually imported.

# AME bindings (MeV)
AME = {"D": 2.224566, "T": 8.481821, "3He": 7.718043, "4He": 28.29566}

def evaluate_occupancy_gap(isotope, Z, N, W_lambda_gate):
    """
    Compare the static Z·N standard-channel prediction against the 
    geometric W_lambda binding to quantify the halo/alpha cluster fraction.
    """
    E_std_bond = 3.89  # MeV, from standard channel
    static_binding = (Z * N) * E_std_bond
    
    # Calculate required dynamic occupancy using the keystone's emitted W_lambda
    E_gate = E0 * mp.log(1 / W_lambda_gate)
    required_occupancy = AME[isotope] / E_gate
    
    return {
        "static_Z_N_binding": static_binding,
        "required_dynamic_occupancy": required_occupancy,
        "delta_MeV": AME[isotope] - static_binding
    }
