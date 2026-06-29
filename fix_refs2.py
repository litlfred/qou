import os
import re

content_dir = "/Users/litlfred/space_cats/qou/content/quantum-observable-universe"

# Map of file names to the bad refs they contain
bad_refs = {
    "simple-objects-V.md": ["rem:fundamental-object-explication"],
    "self-dual-2group.md": ["def:instanton"],
    "p-adic-realisation.md": ["lem:irreducible-connection"],
    "reeb-primes-as-orbits.md": ["chap:algebraic-substrate"],
    "direct-limit-lusztig.md": ["chap:archimedean-universe"],
    "meson-em-sinh-closed-form.md": ["prop:cosh-sinh-q-bridge"],
    "phi-n-global-section.md": ["conj:categorical-neutrality-saturated-shells"],
    "t211-ideal-annihilation.md": ["prop:shell-transition-knot"],
    "topological-mass-formula.md": ["rem:mobius-energy", "sec:small-scale"],
    "pentagon-uv-commutation.md": ["rem:quantum-bloch-group"],
    "gram-determinant-plancherel-ratio.md": ["conj:em-coupling-chern-simons"],
    "qbeta-formalize-first-gates-intro.md": ["sec:mass-algebraic-complex-volume-ladder"],
    "q-beta-c-k-recursion-from-habiro-q-difference.md": ["thm:heat-mode-depth-one-kernel"],
    "phi-q-tower-algebraic-stratification.md": ["conj:phi-q-tower-jsj-bridge"],
    "mass-endomorphism-tower.md": ["prop:jet-gb-pl-correspondence", "prop:sw-period-thimble-equivalence"],
    "chirality-from-frobenius-self-pairing.md": ["prop:six-term-mass-formula-complete"],
    "pre-archimedean-derivation-chain.md": ["prop:jet-convergence-classical-limit", "prop:constit-factor-tau-M-proton-identity", "conj:alpha-cosh-h-z-step-correction"],
    "mass-physical-face-intro.md": ["sec:mass-algebraic-complex-volume-ladder"],
    "q-integer-mass-formula.md": ["rem:per-nucleon-channel-decomposition"],
    "k12-barrier-bypass.md": ["conj:diagrammatic-double-magic-lr-fusion"],
    "fine-structure-observation.md": ["sec:mass-predictions"],
    "p5-counterexample.md": ["conj:blowup-yekutieli"],
    "millennium-unification.md": ["conj:blowup-yekutieli"],
    "definition-index.md": ["lem:ccg-cosimplicial-identities"],
}

for root, _, files in os.walk(content_dir):
    for file in files:
        if file in bad_refs:
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            for ref in bad_refs[file]:
                # replace [text](#ref) with text
                content = re.sub(r'\[([^\]]+)\]\(#' + ref + r'\)', r'\1', content)
            with open(filepath, 'w') as f:
                f.write(content)

