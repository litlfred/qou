"""Fix Context class CamelCase to match file basename's natural CamelCase."""
import re, pathlib, subprocess

def to_pascal(name):
    """Convert any name (snake/camel/Pascal) to PascalCase, preserving inner caps."""
    # Split on underscore
    parts = name.split('_')
    # Capitalize first letter of each part, preserve rest
    out = []
    for p in parts:
        if not p:
            continue
        # If already starts with cap, keep; else capitalize first letter
        out.append(p[0].upper() + p[1:])
    return ''.join(out)

# 17 fixes — explicit table to avoid regression
FIXES = {
    'Frobeniusform': 'FrobeniusForm',
    'Witness12c': 'Witness12C',
    'Witness4he': 'Witness4He',
    'Witness8be': 'Witness8Be',
    'Pernucleonchanneldecomposition': 'PerNucleonChannelDecomposition',
    'Spectatornormalization': 'SpectatorNormalization',
    'Wedderburnweightcanonical': 'WedderburnWeightCanonical',
    'Sdpregimeswitch': 'SDPRegimeSwitch',
    'Qplancherelasymptoticskeleton': 'QPlancherelAsymptoticSkeleton',
    'Inductivegbreduction': 'InductiveGBReduction',
    'Confinementuniversality': 'ConfinementUniversality',
    'Universalilp': 'UniversalILP',
    'Nuclearoperatorregimes': 'NuclearOperatorRegimes',
    'U1equivariantreduction': 'U1EquivariantReduction',
    'Cosimplicial': 'CcgCosimplicialIdentities',
    'Knotparticlegeneration': 'KnotParticleGeneration',
    'Ofweightdecomposition': 'OfWeightDecomposition',
}

files = subprocess.check_output(['find', 'folio/quantum-observable-universe/lean/QOU', '-name', '*.lean']).decode().split()
fixed = 0
for f in files:
    p = pathlib.Path(f)
    if not p.exists():
        continue
    txt = p.read_text()
    new = txt
    for old, new_name in FIXES.items():
        # Replace `OldContext` with `NewContext` (only on word boundary)
        pat = r'\b' + old + r'Context\b'
        new = re.sub(pat, new_name + 'Context', new)
    if new != txt:
        p.write_text(new)
        fixed += 1
        print(f'fixed: {f}')
print(f'Total files: {fixed}')
