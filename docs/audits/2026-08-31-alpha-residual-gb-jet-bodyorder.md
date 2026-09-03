# The α-residual through the GB filtration and the jet tower — it is not four-body

**Bean** `qou-o1dh`. **Probe** `computations/probes/alpha_residual_gb_jet_bodyorder_probe.py`
(4 assertions, all passing). **Owner steer:** redo the α-residual analysis on the
full tower with the Gröbner-base filtration and the jet.

**Headline.** The corpus carries a *"~21 MeV irreducible 4-body α-unit"*
(`t7qv`, `derive_binding_chain_cooperative`). With the two-body input nature
actually supplies, the cluster expansion of ⁴He is **8.90 MeV two-body,
14.60 MeV three-body, 4.79 MeV four-body**. Three-body dominates four-body by
**3.05×**. The corpus's figure is a *pairwise-chain residual*, not a four-body
term, and the genuine irreducible α-unit is ≈ 4.8 MeV.

---

## 1. The two filtrations

### 1.1 Gröbner base filtration — grade = Coxeter length

`computations/gb_filtration_jet_tracker.py`. Grade an element of the
Iwahori–Hecke algebra `H_n(q)` by the Coxeter length `ℓ(w)` of its normal-form
basis elements. The Gröbner–Shirshov reduction has exactly two moves:

```
    T_w · T_i  =  T_{w s_i}                      if ℓ(w s_i) > ℓ(w)   (ascend)
               =  h · T_w  +  T_{w s_i}          otherwise            (descend)

    h = q − q⁻¹        (from the Hecke relation T_i² = h T_i + 1)
```

An **ascent** raises the grade at no cost in `h`. A **descent** splits: the
`h·T_w` term holds the grade and pays one power of `h`; the `T_{w s_i}` term drops
one grade for free.

### 1.2 Jet tower — grade = body order

`computations/binding_manybody_jet_filtration.py`. The many-body expansion of
binding, truncated at the nucleon count `A`:

```
    B(K) = Σ_{n=2}^{A}  m_e · a_D^(n) · w_n(K)

    a_D^(n) = lw(n−1) = (1/n) Σ_{λ ⊢ n} dim_q V_λ        (mean quantum dimension)
```

`a_D^(n)` is the `n`-th Seiberg–Witten period reached through the Yekutieli
non-abelian Stokes route (`QOU.Mass.NaStokesKeystone`). Measured:

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `a_D^(n)` | 1.0000 | 1.0000 | 1.3370 | 2.5328 | 5.3761 | 13.5598 | 37.3678 | 115.8262 |

— super-exponential (successive ratios 1.000, 1.337, 1.894, 2.123, 2.522, 2.756,
3.100). The weight **`w_n(K)` is undetermined**; it is the open `ρ·A` residue
rule. `QOU.Mass.jetBinding_mono` and `jetBinding_lt_succ` prove `B` increases
with `A`, sorry-free.

**The α-residual is by construction the `n = 4` term.** So *"what is the
α-unit?"* is exactly *"what is `w₄`?"*

---

## 2. Where the two filtrations meet

### 2.1 A parity lock between grade and ℏ_q power

Track a word of length `L` through the reduction. Let `a` be the number of
ascents, `b` the number of `h`-branch terms taken, `c` the free descents, so
`a + b + c = L`. The final grade is `g = a − c = 2a + b − L`, hence

```
    b  ≡  g + L    (mod 2)
```

The `h`-power and the GB grade are **locked mod 2**. Checked against the corpus's
own certificate (`gb-filtration-jet-order.witness.json`) for `σ₁³ ∈ H₂`, `L = 3`:

| grade `g` | coefficient | `h`-powers | `g + L` | parity |
|---|---|---|---|---|
| 1 | `q² − 1 + q⁻² = h² + 1` | {0, 2} even | 4 | even ✓ |
| 0 | `h` | {1} odd | 3 | odd ✓ |

### 2.2 The classical limit is the top-grade associated graded

Set `q = 1`, so `h = 0`. Every descending `h`-term dies, `H_n(q)` degenerates to
the group algebra `ℂ[S_n]`, and by Schur–Weyl the Markov trace becomes a
permutation character:

```
    tr_M(β)|_{q=1} = 2^{c(σ_β) − n}
```

With the braid words' cycle counts `c_free = 2A`, `c_atom = A + 1`, `n = 3A`
(verified `A = 2…20`, bean `qou-zrx2`), this is exactly the derived classical
floor

```
    c₀(A) = 2^{2A − 3A} − 2^{(A+1) − 3A} = 2^{−A} − 2^{1−2A}
```

**So the ℏ_q expansion of `qou-zrx2` *is* the GB filtration read by grade**, and
the floor is nothing more exotic than its top-grade associated graded. That
closes the conceptual gap between the two lines of work.

> **Status checked, not assumed.** `GBFiltrationCollapsesAtE2` was demoted from
> `instance` to `def` on 2026-08-24 (bean `qou-fngs`), so it no longer discharges
> itself for every `R` and downstream theorems taking it are genuinely
> conditional. Verified in `QOU/Mathlib/SpectralSequence.lean`, not carried over
> from the older bean.

---

## 3. The empirical input — nature binds one two-body system

This is where the corpus's figure goes wrong. `derive_binding_chain_cooperative`
assigns comparable binding to `pp`, `pn` and `nn` bonds (≈ 2.38, 2.49, 2.53 MeV
in the signed form; 2.91, 3.89, 5.18 in the log form).

**The diproton and the dineutron do not exist.** The deuteron is the *only* bound
two-nucleon system — `³S₁`, `B = 2.22456637 MeV`. The `¹S₀` channel, where `pp`
and `nn` are forced by the Pauli principle, is *just* unbound: virtual states with

```
    a_pp(¹S₀)  ≈  −17.3 fm     (nuclear, Coulomb-corrected)
    a_nn(¹S₀)  ≈  −18.7 fm
    a_np(¹S₀)  ≈  −23.7 fm
```

The honest two-body input is therefore `b₂(pn) = 2.2246`, `b₂(pp) = b₂(nn) = 0`.

---

## 4. The cluster expansion of ⁴He

Ursell–Mayer body-order decomposition, from AME2020 alone. ⁴He = `p p n n` has
pairs `4 pn + 1 pp + 1 nn` and triples `2 ppn + 2 pnn`; the three-body terms come
from ³H and ³He.

```
    b₃(pnn) = B(³H)  − (2 b₂(pn) + b₂(nn)) = 8.48180 − 4.44913 = 4.03266
    b₃(ppn) = B(³He) − (2 b₂(pn) + b₂(pp)) = 7.71805 − 4.44913 = 3.26892
```

| body order | composition | MeV | share of `B(⁴He)` |
|---|---|---|---|
| 2-body | `4·b₂(pn)` | **8.8983** | 31.45 % |
| **3-body** | `2·b₃(ppn) + 2·b₃(pnn)` | **14.6032** | **51.61 %** |
| 4-body | irreducible α unit | **4.7942** | 16.94 % |
| total | `B(⁴He)`, AME2020 | 28.2957 | 100 % |

**Three-body dominates four-body by 3.05×.** The `b₃(pnn) − b₃(ppn) = 0.7637 MeV`
difference is largely Coulomb.

This is the standard nuclear picture: chiral-EFT **three-nucleon** forces are
essential at `A = 3, 4`, while genuine four-nucleon forces are small.

---

## 5. A falsifiable, unfitted constraint on `w_n(K)`

The empirical ⁴He profile **peaks at `n = 3`**. The jet tower at unit weight is
**monotone increasing**:

| n | empirical (MeV) | jet, `m_e·a_D^(n)` (MeV) |
|---|---|---|
| 2 | 8.8983 | 0.5110 |
| 3 | **14.6032** | 0.6832 |
| 4 | 4.7942 | **1.2943** |

A monotone profile cannot reproduce a peak, so the entire shape must come from
the weight:

```
    peak at n = 3    ⟹   w₄/w₃  <  a_D^(3)/a_D^(4)              = 0.52787
    match ⁴He        ⟹   w₄/w₃  =  (b₄/b₃)·(a_D^(3)/a_D^(4))    = 0.17330
```

Both sides are AME data plus the corpus's own `a_D`. No free parameter, nothing
fitted. **Any candidate residue weight that is flat or rising in `n` is excluded
before it is evaluated** — it must fall by at least 1.9× from `n = 3` to `n = 4`,
and by 5.8× to reproduce ⁴He. This is the first falsifiable handle on the open
`ρ·A` rule.

---

## 6. What neither filtration can inform about

**The α-unit's categorical representation** — structurally, not for want of work.

- `a_D^(n) = (1/n) Σ_{λ⊢n} dim_q V_λ` depends **only on `n`**. It averages over
  *all* partitions of `n`, carrying no flavour, no knot type, no linking data. It
  cannot distinguish ⁴He from any other four-body cluster.
- The GB filtration grades a **word** by Coxeter length. Its `q → 1` associated
  graded is a permutation character whose floor depends **only on `A`** — ³H and
  ³He give identical floors, as do ⁵Li and ⁵He (`qou-zrx2`).
- Therefore **every isotope-specific and α-specific fact lives entirely in
  `w_n(K)`**, the undetermined factor. The filtrations organise the expansion;
  they do not populate it.

Concretely: ⁴He is doubly magic (`N = Z = 2`, closed `s`-shell) and its first
excited state sits at **20.21 MeV**, higher than in any other light nucleus. That
exceptional stability *is* the α-unit. Neither `a_D` nor the GB grade contains a
variable that could express it.

---

## 7. What the Standard Model and the eightfold way say

### 7.1 The eightfold way: nothing

Flavour `SU(3)` classifies **hadrons** into multiplets and constrains their
masses through Gell-Mann–Okubo. Nuclear binding is the residual colour force
between colour-*singlet* nucleons — a different regime entirely. There is no
eightfold-way statement about `B(⁴He)`, and the corpus should not expect one.

### 7.2 The Standard Model: in principle, not in practice

QCD determines `B(⁴He)`, but no first-principles closed form exists.

- **Lattice QCD** has bound light nuclei at unphysically heavy pion masses; at
  the physical point ⁴He is at the edge of feasibility and results are not
  settled.
- **Chiral EFT** reproduces `A ≤ 4` binding, but only *with* three-nucleon
  forces whose low-energy constants are fitted. NN-only interactions underbind
  ⁴He by several MeV; the ³H–⁴He correlation (the **Tjon line**) is the standard
  diagnostic.
- **SEMF** is fitted for `A ≳ 20`. Evaluated at `A = 4` with
  `a_V = 15.8, a_S = 18.3, a_C = 0.714, a_A = 23.2, δ = 12/√A`:

  ```
      15.8·4 − 18.3·4^{2/3} − 0.714·2·1/4^{1/3} − 0 + 12/2  =  22.187 MeV
  ```

  against 28.296 — **−21.6 %**. Quoted as context for how badly the collective
  picture does at the α, **not** as a test: `A = 4` is outside the formula's
  domain.

**So the corpus is not failing to reproduce something the SM derives — nobody
derives it.** What the corpus *can* be held to is the **shape**: a body-order
profile peaking at `n = 3`. That is a check the jet tower currently fails at unit
weight, and the `w₄/w₃` bound turns it into a target.

---

## 8. Consequences

1. **The `t7qv` magnitude gate's target should be restated.** It is aimed at
   ~21 MeV; the four-body term is ~4.8 MeV, and most of what it was chasing is
   three-body.
2. **`derive_binding_chain_cooperative`'s `pp`/`nn` bonds have no empirical
   counterpart.** That is a modelling choice and deserves flagging wherever the
   per-bond constants are quoted.
3. **`w₄/w₃ < 0.528`** is the first thing the open `ρ·A` residue rule can be
   tested against before anyone evaluates it.

---

### Provenance

Binding energies AME2020. Scattering lengths and the ⁴He excitation energy are
standard nuclear data, quoted as external context and not derived here. The
cluster expansion uses ³H and ³He as its three-body input, so the `ppn`/`pnn`
split carries Coulomb; the order-of-magnitude conclusion does not depend on that
choice.

-- Ref: [manuscript] bean qou-o1dh; computations/probes/alpha_residual_gb_jet_bodyorder_probe.py
