import sys
content = open('computations/he4_9_3_interface_operator_probe.py').read()
new_code = """
        print(f"  => Total (2,1) trace for λ={lam}: {mp.nstr(total_trace, 6)}")
        
    import json
    from datetime import datetime, timezone
    
    witness = {
        "engine": "python",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "he4_9_3_interface_operator_probe",
        "description": "Option E PROBE 2 A=4 interface operator traces for dominant partitions (nu=(2,1) block).",
        "results": {str(lam): float(total_trace) for lam in results.keys()}
    }
    with open("computations/probes/he4-9-3-interface-operator-probe.witness.json", "w") as f:
        json.dump(witness, f, indent=2)
    print("Wrote computations/probes/he4-9-3-interface-operator-probe.witness.json")
"""
content = content.replace('        print(f"  => Total (2,1) trace for λ={lam}: {mp.nstr(total_trace, 6)}")', new_code)
open('computations/he4_9_3_interface_operator_probe.py', 'w').write(content)
