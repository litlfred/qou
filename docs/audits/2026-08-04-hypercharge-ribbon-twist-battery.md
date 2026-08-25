# T2 audit: hypercharge via ribbon twist — battery results

**Date:** 2026-08-04
**Bean:** `qou-qvpl` (T2), epic `qou-8lxd`
**Script:** `computations/strand_twist_y_battery.py`
**Witness:** `computations/strand-twist-y-battery.witness.json`

## Bottom line

The ribbon-twist candidate `Y_t = 2(T(t)/3 - I₃)` is **highly
constrained** by the spectrum + GMN battery: only 4 of 10,000
helon-style assignments survive. The u-quark and electron twist
multisets are **uniquely determined**.

**STATUS: CANDIDATE FEASIBLE.** The battery passes with no fitted
parameters. But this is candidate-space feasibility, not a derivation:
the twist multisets are enumerated, not derived from the framework's
braid words.

## 1. Battery results

### Search space
- 3 strands per fermion, twist ∈ {-1, 0, +1}
- 10 distinct multisets per flavour
- 4 flavours → 10⁴ = 10,000 total assignments

### Batteries applied
1. **Spectrum:** Y_t must reproduce the SM first-generation
   hypercharge for all 8 chiral states (u_L, d_L, ν_L, e_L, u_R,
   d_R, ν_R, e_R)
2. **Nucleon GMN:** Q_twist = crossing-derived Q on proton (uud)
   and neutron (udd) composites

### Survivors: 4 of 10,000

| Flavour | Surviving multisets | Uniquely determined? |
|---|---|---|
| u | {0, 1, 1} | ✅ YES |
| d | {-1, -1, 1} or {-1, 0, 0} | ❌ 2 options |
| ν | {-1, 0, 1} or {0, 0, 0} | ❌ 2 options |
| e | {-1, -1, -1} | ✅ YES |

### ℤ₆ sanity: ALL PASS

The SM table itself satisfies the Baez-Huerta ℤ₆ compatibility
relation τ/3 + w/2 + Y/2 ∈ ℤ for all 8 states.

## 2. What this proves

### ✅ Proved (enumeration):
- The candidate formula Y = 2(T/3 - I₃) has exactly 4 surviving
  assignments out of 10,000 (p = 4/10000 = 0.04%)
- u-quark twist {0,1,1} and electron twist {-1,-1,-1} are uniquely
  determined by the SM spectrum
- All 4 surviving assignments reproduce the GMN relation on the
  nucleon doublet

### ❌ NOT proved (framework derivation):
- The twist multisets are enumerated, not derived from braid words
- The framework carries no per-chiral-fermion framed braid words
- Q_twist == crossing-derived Q was checked only on the nucleon
  doublet composites

## 3. Anti-fitting assessment

### ✅ CLEAN
- The normalisation T/3 is the colour-tube charge quantum (3 strands
  per quark → divide by 3), structurally fixed
- No fitted parameters anywhere
- Exact rational arithmetic throughout (fractions.Fraction)
- The twist range {-1, 0, +1} is the minimal non-trivial set for
  ribbon-framing integers

### ⚠ SOFT WARNING: helon-model precedent
The twist range {-1, 0, +1} and the 3-strand structure come from
Bilson-Thompson (2005), which IS a literature import. The framework
must independently derive why per-strand twist takes these values.
Currently it does not. This is honest importation of a structural
hypothesis, not a fitted parameter, but it should be derived.

## 4. What's needed to close the bean

1. **Derive** the twist multisets from the framework's braid words
   (the corpus has no framed braid words for chiral fermions yet)
2. **Resolve** the d/ν ambiguity — either derive which option the
   framework selects, or prove both are equivalent
3. **Test** on the second generation (μ, s, c, ν_μ) — the script
   only covers the first generation

## 5. Recommendations

1. ✅ The battery result is significant and should be committed
2. ⚠ The bean stays **open** — feasibility ≠ derivation
3. 📋 New bean: derive per-strand twist from framed braid words
4. 📋 New bean: extend battery to second/third generation
