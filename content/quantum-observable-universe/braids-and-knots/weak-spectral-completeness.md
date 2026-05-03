**Conjecture (weak-sector spectral completeness).**
*The EW/Higgs force-carrier sector $\{T(2,4), T(2,6), T(2,8)\}$
([electroweak/Higgs torus-link triplet](#conj:electroweak-higgs-torus-link-triplet))
admits a **categorically complete idempotent decomposition** in the
Hecke algebra $H_2(q)$:*

$$
  e_W^{+} + e_W^{-} + e_Z^{+} + e_Z^{-} + e_H^{+} + e_H^{-} = \mathbf{1}_{H_2(q)},
$$

*where $e_X^{\pm}$ are the (sym, alt) idempotents corresponding to
the (q^{2k}, q^{-2k}) eigenvalue pair of $T(2, 2k)$ at $k = 2, 3, 4$.
The associated Plancherel weights*

$$
  w_X = \dim_q\bigl(\mathrm{im}\,e_X^{+}\bigr)^2 / [2]_q!
$$

*are categorical constants of the EW sector, calculable from the
substrate parameter $q$ alone.*

### Statement (formal)

The Hecke algebra $H_2(q)$ has Wedderburn decomposition
$H_2(q) \cong \mathbb{Q}(q) \oplus \mathbb{Q}(q)$ with two
1-dimensional blocks (sym and alt), summing to a 2-dimensional
algebra. Each torus link $T(2, 2k) = \sigma_1^{2k}$ acts on these
two blocks with eigenvalues $(q^{2k}, q^{-2k})$
([prop:even-twist-torus-link-psd-feasibility](#conj:electroweak-higgs-torus-link-triplet)).

Define the **per-link block projectors**:
- $e_W^{+} := $ sym block of $T(2, 4)$, $e_W^{-} := $ alt block
- $e_Z^{+} := $ sym block of $T(2, 6)$, $e_Z^{-} := $ alt block
- $e_H^{+} := $ sym block of $T(2, 8)$, $e_H^{-} := $ alt block

These six projectors live in **three different copies** of $H_2(q)$
— one per host surface (genus 1 for $W$, genus 2 for $Z$, genus 3
for $H$). The completeness statement asserts that within the EW
sector, the **direct sum** $e_W^{+} \oplus e_W^{-} \oplus \cdots
\oplus e_H^{-}$ exhausts the Wedderburn-block content of the
combined three-host EW Hecke action.

### Proof sketch (parallels EM spectral completeness)

The argument mirrors
[`thm:em-spectral-completeness`](#thm:em-spectral-completeness)
applied to the two-strand idempotent decomposition $w_+ + w_- = 1$
on the EM sector:

**Step 1 — Per-host two-strand completeness.**
For each $T(2, 2k)$, the two-strand braiding
$\sigma_1 \in B_2$ has the standard Hecke decomposition
$w_+^{(k)} + w_-^{(k)} = \mathbf{1}_{H_2(q)}$ where $w_\pm^{(k)}$
are the (sym, alt) idempotents acting on $V \otimes V$ for the
$k$-th host's natural representation $V_k$.

**Step 2 — EW sector is the direct sum across hosts.**
The three hosts $\Sigma_1^W, \Sigma_2^Z, \Sigma_3^H$ are
inequivalent as $\hat\tau$-equivariant covers
([conj:force-carrier-knot-vs-link-dichotomy](#conj:force-carrier-knot-vs-link-dichotomy)),
so their $H_2(q)$ Wedderburn decompositions live in independent
direct summands. The EW total Hecke action is therefore
$\bigoplus_{k=2,3,4} H_2(q)_k$, with completeness across the
direct sum following from per-host completeness in Step 1.

**Step 3 — Plancherel weight assignment.**
For each $k$, $\dim_q(\mathrm{im}\,e_W^{+}) = 1$ (the 1-dimensional
sym block) and $[2]_q! = [2]_q$. So:

$$
  w_X^{(k, \pm)} \;=\; 1^2 / [2]_q \;=\; 1 / [2]_q
$$

a *uniform* Plancherel weight across all six EW idempotents at any
fixed $q$. This uniformity is the **completeness signature** —
contrast EM, where the Bring-saturating $T_{2,9}$ and $T_{3,5}$
have *non-uniform* weights $[9]_q$ and $[10]_q$.

The uniform-weight identity is what closes the EW spectral
completeness once the host-distinctness conjecture (U2) is
discharged.

### Downstream consequence — closes NV-1

The weak-scale crossing count $N_v$ is conjecturally the
**Plancherel-weighted Hecke-trace product** over the EW
force-carrier sector:

$$
  N_v \;\stackrel{?}{=}\; \prod_{k = 2, 3, 4}
  \frac{\dim_q(T(2, 2k))^2}{[2]_q}
  \cdot \mathcal{N}_{\rm sym}(q),
$$

where $\dim_q(T(2, 2k)) = [2k]_q$ is the q-dimension of the
$T(2, 2k)$ representation
([Hecke-Skein convention §7a](https://github.com/litlfred/qou/blob/main/CLAUDE.md))
and $\mathcal{N}_{\rm sym}(q)$ is a categorical normalization
constant from the symmetric channel.

**PSLQ test status.** When this conjecture is discharged, the
basis $\{[4]_q^2/[2]_q, [6]_q^2/[2]_q, [8]_q^2/[2]_q,
\mathcal{N}_{\rm sym}(q)\}$ becomes available. PSLQ at 1000 dps
on this *extended* basis would test whether $N_v$ admits the
conjectured product form. The earlier negative PSLQ result
([nv-pslq-uniqueness-probe.witness.json](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/nv-pslq-uniqueness-probe.witness.json))
in the *unextended* basis is consistent with the closed form
requiring this Plancherel structure.

### Status

🟡 **Open**. Requires three prerequisite conjectures
(U2 + U4 + U2's Higgs-mechanism extension); none currently
provable in QOU's existing framework (per
`docs/audits/2026-05-02-nv-frob-filter-conjectures.md`).

**To promote to `proposition`:**
1. Discharge U2
   ([conj:force-carrier-knot-vs-link-dichotomy](#conj:force-carrier-knot-vs-link-dichotomy))
   — categorical Higgs mechanism in $\mathbf{Rep}$-language.
2. Discharge U4
   ([conj:electroweak-mass-eigenstate-count](#conj:electroweak-mass-eigenstate-count))
   — categorical broken-Wedderburn split.
3. Author $\mathcal{N}_{\rm sym}(q)$ — the symmetric-channel
   normalization, analog of the Plancherel ratio in
   [`prop:gram-determinant-plancherel-ratio`](#prop:gram-determinant-plancherel-ratio).
4. Run PSLQ at 1000 dps on the extended basis to verify the
   closed-form prediction for $N_v$.

### Audit-flag impact

If this conjecture closes:
- **NV-1**: 🔴 → 🟢 (closed via PSLQ on extended basis)
- **β-decay rates**: $G_F = 1/(\sqrt{2}\,N_v^2 E_\times^2 \mu_0^2)$
  becomes derivable from $(q_0, m_e)$ alone, closing every β-decay
  half-life prediction simultaneously.
