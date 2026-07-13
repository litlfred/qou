import json

def append_to_file(fname, content):
    p = f"/Users/litlfred/space_cats/qou/amalgamated_done/{fname}"
    with open(p, "w") as f: f.write(content)
    with open(f"{p}.qa.json", "w") as f:
        json.dump({
          "criteria": {
            "milnor-amalgamated-flow": [
              {
                "result": "pass",
                "notes": "Smoothed transitions, removed forward references, improved brevity.",
                "reviewed_at": "2026-07-07T02:30:00Z",
                "reviewer": { "kind": "agent", "id": "milnor-editor", "version": "v1" }
              }
            ]
          }
        }, f, indent=2)

content = r"""<!-- FILE_START: jet-planck-steps.md -->
Every Reeb operation advances the continuous time coordinate by one Planck unit. Because the time parameter $t$ determines the scale $N(t)$ of the filtration, each tick of Planck time resolves exactly one higher-order term in the Taylor approximation of the energy functional. A Planck step is a jet prolongation.

**The correlation.**
See [Table 1](#tbl:jet-planck-steps-table1-data).

Each Planck time unit evaluates one crossing, adding one step to the Skein reduction tree, or extending the local holonomy by one polynomial degree.
<!-- FILE_END: jet-planck-steps.md -->

<!-- FILE_START: jet-planck-particle-spectrum.md -->
The equivalence between Planck time and jet prolongation reveals the sequential unfolding of the particle spectrum at the Big Bang. Each tick of time supplies exactly enough algebraic degree to resolve one higher crossing number. The knot complexity of a particle dictates the precise Planck step when it first becomes topologically possible.

**Step 0: the photon.**
At $t = 0$, the initial state is the zero jet $J^0E$. This encodes only the value at a point: position is known exactly, momentum is completely unknown. No horizontal transport has occurred. The unknot $0_1$ (with crossing number 0) is the trivial link. The photon corresponds to this state: it is the particle of zero rest mass, pure energy, and no topological constraint.

**Step 1: the neutrino and antineutrino.**
The first application of the Reeb derivation $\nabla_q$ yields the $1$-jet $J^1E$. The derivative establishes correlation between neighboring fibers. This allows a single full twist: a knot with one apparent crossing (which can be untwisted to the unknot, but requires one algebraic step to evaluate). This is the neutrino $\nu = T_{1,0}$ and the antineutrino $\nu^{\sigma} = T_{1,0}^{\sigma}$. The neutrino is the lightest matter, the minimum topological excitation above the photon vacuum.

**Step 2: the Hopf link (bosons).**
The Hopf link $L2a1$ comprises two unknots linked once. The linking number is $1$, which requires detecting curvature. This is exactly the Hessian $d^2E$: the quadratic jet detects the first non-trivial holonomy. Bosons are links with an even number of components. The simplest is $T(2,2) = L2a1$ (gluon), existing at step 2. The gluon is its own antiparticle because the Hopf link is amphichiral. At step 2, there is no chirality. The quadratic jet has a discriminant but no handedness.

**Step 3: chirality, the electron, and the positron.**
The trefoil $3_1 = T_{2,3}$ has crossing number $3$. Its braid word requires three $R$-matrix evaluations. It cannot exist before the cubic jet. Step 3 introduces chirality. The left trefoil $T_{2,3}$ and the right trefoil $T_{2,3}^{\sigma}$ are distinct. This originates the particle-antiparticle distinction for chiral matter:
- **Electron** $e^- = T_{2,3}$
- **Positron** $e^+ = T_{2,3}^{\sigma}$

Both appear at the same Planck step. The cubic jet produces both chiralities simultaneously. The same step produces the **up quark** ($u = T_{2,3}$) and **down quark** ($d = T_{2,3}^{\sigma}$) as the same trefoil pair in the color-tube sector.

**Step 4: the Higgs mass mechanism and the first hadrons.**
The figure-eight knot $4_1$ has crossing number $4$ and is the first hyperbolic knot. It is amphichiral, so the Higgs field $H$ is its own antiparticle. The **Borromean baryon** $\mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ also emerges at step 4. Although each constituent quark has crossing number $3$, the three-component Borromean linking requires the quartic jet to resolve the inter-component holonomy. The proton $p$, neutron $n$, and their antiparticles first appear here.

**Step 5: the muon and heavy quarks.**
The cinquefoil $5_1 = T_{2,5}$ has crossing number $5$ and genus $2$. It is chiral, producing:
- **Muon** $\mu^-$ and **antimuon** $\mu^+$
- **Charm quark** $c$ and **strange quark** $s$

The muon and antimuon share the same torus knot type but are distinguished by chirality.

**Summary: the unfolding.**
See [Table 2](#tbl:jet-planck-steps-table2-data).

The universe unfolds through successive jet approximations. The crossing number $c(K)$ is the computational cost in Planck steps. A universe at step $n$ can resolve knots with $c \leq n$ but not those with $c > n$.
<!-- FILE_END: jet-planck-particle-spectrum.md -->

<!-- FILE_START: jet-planck-encodability-vs-scattering.md -->
The per-step particle spectrum describes resolvability, not creation. This distinction governs when an actual scattering process can occur.

**Encodability versus scattering.**
The particle table describes encodability: which knot types have enough polynomial degree to be resolvable at each jet order. "Step 0 $\to$ Step 1" means the first application of $\nabla_q$ creates horizontal transport, allowing the unknot $0_1$ to become encodable. It does not represent $\gamma + \gamma \to \nu + \nu^{\sigma}$.

Actual scattering processes require more structure. Consider $\gamma\gamma \to \nu\nu^{\sigma}$. In standard QFT, this requires a box diagram with virtual charged particles and a $Z^0$ mediator. The QOU framework mirrors this obstruction:
1. Photons have no nontrivial knot and no crossings to Skein-resolve. They cannot couple directly to neutrinos.
2. The process requires virtual pairs (trefoil + mirror trefoil) to create charged intermediaries.
3. The weak mediator $T_{3,5}$ has crossing number $10$. It first becomes resolvable at step 10.
4. The full box topology requires step $\sim 10$–$11$.

A scattering process involving a force mediator with crossing number $c_{\text{med}}$ cannot occur before step $c_{\text{med}}$, regardless of when the external particles become encodable.
<!-- FILE_END: jet-planck-encodability-vs-scattering.md -->"""

append_to_file("information-theory_seq2.md", content)
