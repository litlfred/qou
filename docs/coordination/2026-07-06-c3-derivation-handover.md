# 2026-07-06: $c_3$ Derivation Handover

## 1. Branch Merge Prepared
- `feature/type-b-crystal-infra` has been merged to `main`. This includes the foundational Kashiwara Python logic. 

## 2. Structural Dead Ends (Refuted)
All KLR/crystal composite structures initially scoped have been explicitly **REFUTED** by the `computations/qbeta/qbeta_klr_composite3_preflight_run.py` preflight sign analysis:
- **Option B (Wenzl $\times$ q-Pochhammer)**
- **Option C (Demazure $\times$ q-Pochhammer)**
- **Option D (Type-B folded crystal sum)**

**Why they fail:** The $c_k$ ladder requires the constraint $c_2 = -1 < 0$. However, the sum over positive $q$-contents in these composites produces strictly positive coefficients ($c_2 > 0$) because there is no q-Pochhammer or parity factor to flip the sign at $u^2$.

## 3. The Live Path: The Hyperbolic Phase Series
With the categorical combinatorial structures exhausted, the only surviving, mathematically active pathway to derive $c_3$ is the **Hyperbolic Phase Series** (identified in the `docs/coordination/1ppq-qbeta.md` ledger on 2026-06-05).

The precision ladder is a Taylor expansion of a single hyperbolic phase:
$$ \frac{Q_\beta}{Q_A} = \cos(\Phi(u)) $$
where $\Phi(u) = \Phi_1 u + \Phi_2 u^2 + \dots$

Expanding the cosine gives:
- $c_2 = -\frac{\Phi_1^2}{2}$
- $c_3 = -\Phi_1 \Phi_2$

Since $c_2 = -1$ is Taylor-exact, this proves that **$\Phi_1 = \sqrt{2}$**.
Thus, $c_3 = -\sqrt{2} \Phi_2$. 

To derive $c_3$, we must isolate the algebraic origin of $\Phi_2$. This is fundamentally tied to the Reeb-bundle `sinh` holonomy and the Hoefsmit $H_3(q)$ kernel parameters (the `alpha_eff` bar-ODD wrap angle).

## 4. Next Step: "More Depth"
The immediate priority is to examine `probe_q_beta_operator_valued_N3.py` which contains the symbolic `alpha_eff` ($\alpha = (z-1) \cdot h / 2$). We must connect this explicit $\alpha$ to the $c_k$ recursion kernel to extract the theoretical value of $\Phi_2$.
