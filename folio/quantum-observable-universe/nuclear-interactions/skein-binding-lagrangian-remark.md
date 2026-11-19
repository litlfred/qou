Each term of the [canonical binding Lagrangian](#def:skein-binding-lagrangian) arises from the exact evaluation of the topological trace on the link components, without empirical liquid-drop parameters.

1. **Strong binding (q-CLT/JSJ volume term).** The strong force contribution evaluates strictly from the Hecke channel traces. As established in [q-CLT mass scaling](../mass-theory/q-clt-jsj-mass-scaling.md), the Jaco–Shalen–Johannson decomposition yields an additive scaling for the strong binding:
   $$
     \mathcal{L}_{\mathrm{qCLT}}
     = \alpha \sum_i \ln\lvert V_i\rvert,
   $$
   where $\alpha = \mathfrak{m}_e / (q_0(q_0-1))$ is the rigid substrate scale (built from CAL-1 $\mathfrak{m}_e$ and CAL-2 $q_0$), and $V_i$ are the two-nucleon sub-braid Markov traces for each bond type. This carries no empirical parameter beyond that calibration scale, and is **intended** to replace the empirical Bethe-Weizsäcker volume, surface, asymmetry, and pairing terms — but that replacement is **not a completed closure**: the per-isotope binding magnitude ($\Delta_\lambda$) is open, so its empirical accuracy against AME is not established here.

2. **Coulomb repulsion.** Each proton--proton crossing acquires a $q$-deformed wedge product asymmetry. The categorical difference between identical-chirality crossings (coefficient $q$) and mixed crossings evaluates directly to the electrostatic penalty. As mapped by the $\mathrm{U}(1)$ sub-action:
   $$
     \mathcal{L}_{\mathrm{Coulomb}} = E_C(Z, A),
   $$
   which recovers the standard $\approx 0.71\, Z(Z-1)/A^{1/3}$ MeV Coulomb energy from the $\mathrm{U}(1)$ sub-action. A witness now exists: [`mirror-split-continuum-em`](../../../computations/deltalambda/mirror-split-continuum-em.witness.json), computed by [`coulomb_energy.py`](../../../computations/coulomb_energy.py) with **zero fitted constants** — the fine-structure constant from the derived trace ratio $1/(q_0 [9]_q [10]_q)$ and the length from the CAL-3 scale $\hbar c / \mathfrak{m}_\pi$, not the empirical $r_0$. On the mirror pair it gives $\Delta E_C \approx 0.847$ MeV against an observed $0.764$ MeV, i.e. $+10.9\%$.

   Two steps in that recovery are selections rather than derivations, and the producer flags both in its own comments. The $A^{1/3}$ packing law is **not derived**: solving for the exponent against measured radii gives $0.43$ at $^3\mathrm{H}$ and $0.53$ at $^3\mathrm{He}$, so the residual is a radius that is roughly a fifth too small rather than a small correction. The uniform-sphere geometry factor $3/5$ is likewise a choice whose alternatives bracket the answer ($3/5 \to 0.849$, $1/2 \to 0.707$, against $0.764$ observed). So the match is a genuine zero-parameter evaluation, not yet a categorical derivation of $a_C$.
