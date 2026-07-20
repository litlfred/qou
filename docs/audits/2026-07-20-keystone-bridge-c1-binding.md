# Keystone bridge C1 ↔ binding module: the normalized binding OGF satisfies the proved q-lift kernel — PROVED (normalization leg)

**Date:** 2026-07-20
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Bean:** `qou-55uw`
**Status:** AUDIT — a PROVED (sorry-free) discharge of the *normalization/recurrence*
leg of the Tier-1 keystone
[`conj:binding-manybody-eq-jet-filtration`](../../content/quantum-observable-universe/mass-theory/binding-manybody-jet-filtration.md)
/ [`conj:qdifference-kernel-prolongation-symbol`](../../content/quantum-observable-universe/mass-theory/qdifference-kernel-prolongation-symbol.md).
The GEOMETRIC identification leg stays conjectural (§3). Companion to the
2026-07-20 confluent-narrowing audit (which excluded the *raw-OGF* carrier).

## 0. Summary

The keystone claims the proved confluent q-lift kernel **C1**
(`QOU.Mass.QDifferenceConfluentObstruction.qlift_normalized_kernel_exists`,
classically `normalized_classical_kernel_exists`) is the generating structure of
the BINDING series. The obstacle was a **normalization mismatch** between two
proved objects:

- **C1 carrier** proved so far: `b_n = f_n/[n]_q!` (q-factorial normalized;
  classically `f_n/n!`, the involution EGF coefficient), satisfying
  `[n+2]_q·b_{n+2} = b_{n+1} + b_n`.
- **Binding period** (proved corpus, `sw-classical-jet-exactness`;
  `BindingGevreyHalf`): `a_D^{(n)} = f_n/n` (`f=I`, the involution/telephone
  numbers; the `q=1` value of `S(n)=Σ_{λ⊢n} dim_q λ`), so the body term is
  `B_n = m_e·f_n/n`.

**These differ by a fixed factorial (q-Borel) strip, worked exactly.** Demanding
the transform `b_n = B_n/N(n)` land on the C1 carrier:

```
   m_e·f_n /(n·N(n))  =  m_e·f_n / n!   ⟺   n·N(n) = n!   ⟺   N(n) = (n−1)!.
```

So the **unique fixed normalizer** is
| leg | N(n) |
|-----|------|
| classical | `N(n) = (n−1)!` |
| q-lift | `N_q(n) = [n−1]_q! = qfact q (n−1)` |

Under it the normalized binding OGF is **exactly** the C1 carrier, hence
satisfies the proved kernel — the constant `m_e` cancels (the kernel is linear
homogeneous). **No obstruction, no fit; the normalizer is forced by
`n·N(n)=n!`.** This is the §5 "survivor" of the confluent-narrowing audit made
precise: the raw OGF fails (super-geometric growth vs bounded-depth), the
`(n−1)!`-stripped (Gevrey-1/2 Borel) OGF succeeds.

## 1. What is PROVED (sorry-free, lean-direct exit 0)

New file
[`QOU/Mass/KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean)
(wired into `QOU.lean`; verified `lean`-direct against the restored `v4-24-0`
olean cache):

| theorem | statement |
|---------|-----------|
| `period_carrier_strip` | `f_{m+1}/(m+1) = (f_{m+1}/(m+1)!)·m!` — exhibits `N(n)=(n−1)!` (via `n·N(n)=n!`). |
| `keystone_bridge_binding_classical` | for any `f` with `f(n+2)=f(n+1)+(n+1)f(n)`, the `(n−1)!`-normalized period `b_k = m_e·(f_k/k)/(k−1)!` satisfies `(n+2)·b_{n+2}=b_{n+1}+b_n`. |
| `keystone_bridge_binding_qlift` | q-lift over a field with non-vanishing q-integers: for `S(n+2)=S(n+1)+[n+1]_q·S(n)`, the `[n−1]_q!`-normalized q-natural period satisfies `[n+2]_q·b_{n+2}=b_{n+1}+b_n`, `c(q)=1`. |
| `keystone_bridge_involution` | concrete discharge on `involutionNumber` (recurrence holds by `rfl`): the classical na-Stokes period `I(n)/n`, `(n−1)!`-normalized, satisfies the proved depth-2 kernel. |

Base ring: classical over `ℚ` (pre-archimedean, no ordering beyond ℚ — §7c
wall-safe, no `ℝ`); q-lift over generic `[Field K]`. Indices shifted `n+1,n+2,n+3`
so every `/k` and `(k−1)!` is division-safe (no ℕ-subtraction). The
**correct base ring matters**: an earlier uncommitted attempt on this branch
stated the strip over a generic `[Field K]` and died on `positivity`
(`PartialOrder K` unsynthesizable) — over a field of characteristic dividing
`m+1`, `(m+1)` and the factorials can VANISH and the identity is false. The
proved version is over `ℚ` (classical) / with explicit `qint ≠ 0` hypotheses
(q-lift). That broken hunk was reverted; this file re-derives it correctly.

## 2. Exactly what this DISCHARGES

The keystone's carrier/normalization leg: **the binding module (period `I(n)/n`),
under the forced q-Borel normalizer `N(n)=(n−1)!`, IS the C1 carrier and
therefore obeys the proved depth-2 (q-)difference kernel.** The empirical
"`ρ·A`" scale rule is thereby an *output* of the C1 recursion applied to the
normalized series, not a fitted constant — for the recurrence/normalization
content. Combined with the confluent-narrowing audit, the picture is complete at
the recurrence level: raw OGF excluded, `(n−1)!`-normalized OGF governed by C1.

## 3. What stays CONJECTURAL (the honest residual — NOT proved)

1. **The geometric identification.** That this depth-2 carrier IS the
   Seiberg–Witten **prolongation symbol** — i.e. that the C1 kernel *arises from*
   the fibre root-of-unity singularity structure of `λ_SW`
   (`prop:sw-period-residue-sum`) — is the content of
   `conj:qdifference-kernel-prolongation-symbol` and is **untouched** here. We
   proved a recurrence/normalization identity between two *already-known*
   sequences; we did **not** derive the kernel from the geometry. Per
   §Axiomatization-is-not-a-Proof: a proved normalization is not a proved
   geometric origin. This remains a conjecture; nothing here should be wired to
   production as "prolongation symbol proved".
2. **The q-natural period choice (`/[n]_q` vs `/n`).** The q-lift bridge is
   stated for the q-natural period `S(n)/[n]_q` (replacing the manuscript's
   plain-integer `a_D^{(n)}=S(n)/n` by `n→[n]_q`, matching the `dim_q`
   q-deformation of `S(n)`). At `q=1` both coincide (`[n]_1=n`) so the
   **classical** leg matches the manuscript's `a_D^{(n)}=I(n)/n` unconditionally.
   For `q≠1` the promotion `/n → /[n]_q` is a fibre-natural **definitional
   choice**, not a fit; if the manuscript intends the literal plain-`/n` period,
   the exact q-lift normalizer is instead `[n]_q!/n` (not a clean q-factorial) —
   a real wrinkle flagged, not fudged.
3. **The many-body / few-body truncation** (`w_n(K)` weights, sum-to-A vs
   few-body) is a separate open question (`binding-manybody-jet-filtration.md`
   scope note) untouched here.

## 4. Discipline

- **Corpus-grep / formalize-first.** This is the forward-pruning complement to
  the 2026-07-20 confluent-narrowing audit: that audit excluded the raw-OGF
  carrier (super-geometric growth); this one *constructs* the surviving
  normalized carrier and proves it satisfies C1. No prior corpus artifact stated
  the exact `N(n)=(n−1)!` reconciliation (the abandoned branch hunk attempted it
  but was broken/uncommitted).
- **Anti-fit.** The normalizer is forced by `n·N(n)=n!`; both inputs (period
  `I(n)/n`, carrier `I(n)/n!`) are proved corpus facts. Nothing fitted.
- **Scope honesty.** DERIVED = normalization + recurrence (§1–2). CONJECTURAL =
  geometry + q-natural period choice (§3). The two are labelled separately and
  the geometric leg is not claimed.
