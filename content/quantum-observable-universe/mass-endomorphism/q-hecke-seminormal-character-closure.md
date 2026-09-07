# Partition-sum Wedderburn decomposition of the Markov trace

$$
  \mathrm{tr}_M^{\mathrm{partition\text{-}sum}}(\mathcal{B}_K)
  \;:=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q) \cdot \mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda^q(\mathcal{B}_K)\bigr),
$$

This partition-sum form equals the canonical Markov-axiom reducer $\mathrm{tr}_M(\mathcal{B}_K)$ ([`prop:markov-trace-recursive-reducer`](#prop:markov-trace-recursive-reducer)) to numerical precision at $q = q_0$.

## Significance

The partition-sum form rewrites the Markov trace via the Wedderburn–Artin decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}(\mathbb{C})$. The result `prop:hecke-branching-trace-decomposition` relies on this decomposition. Downstream consumers (such as binding-energy analysis via $\rho_K$ refinement and force-carrier saturation identities) require a partition-by-partition decomposition of $\mathrm{tr}_M$ that the recursive reducer does not directly expose.

The recursive Markov-axiom ascent and partition-sum Wedderburn formulas must agree. The agreement was previously broken at $q \ne 1$ due to a character convention error. `schur_weyl_symbolic.specht_character_atomic` incorrectly returned the classical Murnaghan–Nakayama character $\chi^\lambda_{\mathrm{MN}}(\pi(\beta))$ at $q = 1$ instead of the $q$-Hecke character $\chi^\lambda_q(\beta)$.

Two layers have to be got right, and each has a natural wrong answer:

1. **Weight layer.** The weight is $y_\lambda(q)$, the Wenzl Schur principal specialisation (`prop:hecke-branching-trace-decomposition`), and what distinguishes it from the naive two-variable Schur function $s_\lambda(q, q^{-1}) / H_q(\lambda)$ is the **normalisation**: $y_\lambda$ divides by $Z = \sum_\mu s_\mu f^\mu$, fixed by $\sum_\lambda y_\lambda f^\lambda = \mathrm{tr}_M(1) = 1$, not by the hook polynomial $H_q(\lambda)$.
2. **Character layer.** The $q = 1$ limit of the Hecke character is not the character required here; the trace must be taken of the $q$-Hecke character $\chi^\lambda_q(\mathcal{B}_K) = \mathrm{tr}\,\rho_\lambda^q(\mathcal{B}_K)$, via Hoefsmit seminormal matrices at $q_0$.

> **Corrected 2026-09-06** (`qou-fq0f`). Bullet 1 used to discriminate on
> *vanishing*: that $s_\lambda(q,q^{-1})/H_q(\lambda)$ "vanishes for partitions
> with three or more rows and so cannot serve as the weight". Under production
> convention **D** that reason is vacuous, because $y_\lambda(q)$ vanishes there
> too — see the row cap below. It was a **convention-C argument**, true when
> written and left untouched by the C → D migration of 2026-08-09.

### The sum is over at most two rows

Under the production convention $z = q^3/(q^2+1)$ the displayed sum is **not**
over all partitions of $3A$, however it is written. The Wenzl level is fixed by
$Q^{r} = z_W/(1 - Q + z_W)$ with $Q = q^2$, $z_W = qz$, and convention D gives

$$
  1 - q^2 + \frac{q^4}{q^2+1} \;=\; \frac{1}{q^2+1}
  \qquad\Longrightarrow\qquad
  Q^{r} \;=\; q^4 \;=\; Q^2, \qquad r = 2 \ \text{ exactly.}
$$

Wenzl's row cap ($s_{\alpha,r} = 0$ whenever $\ell(\alpha) > r$; Orellana,
*Crelle* **508** (1999) 157–178, p. 5) therefore bites at two rows, so
$y_\lambda(q) = 0$ for every $\lambda$ with three or more rows and
$\mathrm{tr}_M$ factors through the two-row (Temperley–Lieb) quotient:

| | partitions | carry weight under **D** | annihilated |
|---|---|---|---|
| $H_3$ | $(3), (2,1), (1,1,1)$ | $(3), (2,1)$ | $(1,1,1)$ |
| $H_4$ | 5 shapes | $(4), (3,1), (2,2)$ | $(2,1,1), (1,1,1,1)$ |

These are algebraic zeros, not small residuals: the $H_4$ closed forms carry a
literal factor $(A z - q^3)$ with $A = q^2+1$, and $z_D = q^3/A$ is its root
(`h4_markov_weights_closed_form.py`, asserted at run time). Two independent
paths agree exactly — the Wenzl specialisation `y_lambda_symbolic` and that
closed-form substitution — and both give $w^D_\lambda = s_\lambda(q,q^{-1})/[2]_q^4$
on the surviving shapes with $\sum_\lambda w_\lambda d_\lambda = 1$.

**Convention C did not cap anything.** There $r \approx 2.5995$ — not an integer
— which is why the C-frame weights were non-zero on three-row shapes and why
bullet 1's original contrast read as decisive. That D lands on an *integral*
Wenzl level and C does not is a derivation-side argument for D that has not been
written down anywhere else; it is flagged for the owner in `qou-fq0f`.

## Numerical verification

| Atom | $|\mathrm{tr}_M|$ (convention **D**, muon pin) |
|---|---:|
| Proton | $0.62932842249$ |
| Neutron | $0.47513351767$ |
| Deuteron | $0.15196834396$ |
| Tritium | $0.02914404235$ |
| ${}^3$He | $0.05859625835$ |

> **Ordering corrected 2026-09-05** (`qou-hu1f`). Earlier the same day these
> values were migrated C → D from `atomic-tr-m-mpfr-50dps.witness.json` — which
> was computed **2026-08-29, before** the intra-ordering owner ruling, and had
> never been regenerated. The producer has now been re-run under the ruling and
> the table takes its output:
>
> | atom | grouped (superseded) | **borromean (the ruling)** |
> |---|---:|---:|
> | Proton | $1.14575978232$ | $0.62932842249$ |
> | Neutron | $0.98774375682$ | $0.47513351767$ |
> | Deuteron | $0.57517232973$ | $0.15196834396$ |
> | Tritium | $0.22931014615$ | $0.02914404235$ |
> | ${}^3$He | $0.40376713691$ | $0.05859625835$ |
>
> A factor of $1.8$ to $7.9$, growing with $A$ — far larger than the convention
> migration that preceded it. `atom_braid_word_3A` lays each nucleon's
> confinement core down alternating, `(σ₀σ₁⁻¹)³`, because `σ₀` and `σ₁` do not
> commute and only the alternating word is `β_Bor`.
>
> Both axes are now current: **convention D** and the **borromean** ordering, at
> the muon pin, all three taken from the producer rather than substituted by hand.

> **Migrated C → D, 2026-09-05** (`qou-i229` → `qou-46ab`, owner-approved:
> *"refresh and migrate"*). Source: the canonical Hoefsmit + Wenzl bridge witness
> `atomic-tr-m-mpfr-50dps.witness.json`, which computes these five atoms by this
> block's own stated method $\sum_\lambda y_\lambda \chi_\lambda$ at
> `q0Anchor: muon`.
>
> | atom | was (convention C) | now (convention D) | ratio |
> |---|---:|---:|---:|
> | Proton | $1.06530622859$ | $1.14575978232$ | $1.0755$ |
> | Neutron | $0.92323329717$ | $0.98774375682$ | $1.0699$ |
> | Deuteron | $0.38828647155$ | $0.57517232973$ | $1.4813$ |
> | Tritium | $0.10405211868$ | $0.22931014615$ | $2.2038$ |
> | ${}^3$He | $0.20654085856$ | $0.40376713691$ | $1.9549$ |
>
> The proton ratio is `qou-46ab`'s signature, established there to 50 digits:
> C-frame $1.0653062286131670594$ against D-frame $1.1457597822878355047$,
> $|D-C|/C = 0.0755215$.
>
> **The anchor is unchanged.** The C table was muon-anchored — its per-atom
> $D/C$ ratios match `qou-46ab`'s convention ratio at the muon pin to 8 digits
> and at the proton pin only to 7 — so this is a convention migration, not a
> re-anchoring. The muon pin used is the live one, the same target as the
> `q₀` refresh in this pass.
>
> **The two-column form is withdrawn, not recomputed.** The table used to print
> $|\mathrm{tr}_M|$ *canonical* against *partition-sum* with a $\sim 10^{-15}$
> "relative error", and that column read as a verification of the values. It was
> not: it was the agreement of **two C-frame paths**, which says nothing about
> which convention both are in. The character-closure identity is
> convention-independent and the declaring probe verifies it on abstract braids,
> so the two paths agree under D as well — but **that agreement has not been
> re-measured at these five nuclei**, because the second path is `markov_peel`,
> whose proton and neutron entries `qou-46ab` deliberately removed as unreliable
> (`canonical_tr_m_three_path_comparison.py`). Printing a residual nobody has
> measured would repeat the defect this migration is fixing.

## Production paths

The values above come from the canonical Hoefsmit + Wenzl bridge,
`atomic-tr-m-mpfr-50dps.witness.json`, under the production convention **D**.

The earlier claim that "all three paths agree at the precision floor of their
respective layers" is **withdrawn as stated**: that agreement was measured
within convention C, and `canonical_tr_m_three_path_comparison.py` records that
the three paths do *not* all agree under D — `pyhecke` SW disagrees by orders of
magnitude and the legacy path by ~15 % — while `markov_peel`'s proton and
neutron entries were deliberately removed as unreliable (`qou-46ab`). What holds
is the narrower statement the block actually needs: bridge ≡ `markov_peel` where
both are recorded.

The declaring witness, `q-hecke-seminormal-character-closure-probe`, verifies the
character-closure identity on five **abstract** $B_3$ braids (identity,
$\sigma_1$, the Coxeter element, the figure-8, the full twist) and contains no
nucleon, so it is a structural verifier of the identity — which is
convention-independent — and not the producer of this table.
