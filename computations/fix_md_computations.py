import os

content_dir = "/home/litlfred/space_cats/qou/content/quantum-observable-universe/molecular-construction"

missing_computations = {
    "ilp-covalent-bond.ts": [
        "folio-assistant/computations/molecular-experimental-refs.witness.json"
    ],
    "co-triple-bond-energy.ts": [
        "folio-assistant/computations/co-bond-order-active-set.witness.json"
    ],
    "co2-molecular-braid.ts": [
        "folio-assistant/computations/molecular-experimental-refs.witness.json"
    ],
    "co2-lp-dual-binding.ts": [
        "folio-assistant/computations/co-bond-order-active-set.witness.json",
        "folio-assistant/computations/molecular-experimental-refs.witness.json"
    ],
    "benzene-threading-emergence.ts": [
        "folio-assistant/computations/molecular-experimental-refs.witness.json"
    ],
    "benzene-bond-equalization.ts": [
        "folio-assistant/computations/molecular-experimental-refs.witness.json"
    ]
}

for root, dirs, files in os.walk(content_dir):
    for filename in files:
        if filename in missing_computations:
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as f:
                content = f.read()
            
            if "computation:" not in content:
                print(f"Fixing {filepath}")
                
                witnesses_str = ",\n      ".join(f'"{w}"' for w in missing_computations[filename])
                comp_block = f"""  computation: {{
    engine: "python",
    witness: [
      {witnesses_str}
    ],
    status: "experimental",
  }},"""
                
                # Insert before the last closing brace
                new_content = content.replace("\n});", f",\n{comp_block}\n}});")
                with open(filepath, 'w') as f:
                    f.write(new_content)
            else:
                print(f"Skipping {filepath} (computation field already exists)")
