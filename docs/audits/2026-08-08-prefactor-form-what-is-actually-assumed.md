# The prefactor form: the ledger names the wrong thing, and two registered references were never consulted

**Date:** 2026-08-08 · **Beans:** `qou-fl4t`, `qou-pn5j`
**Amends:** `docs/audits/2026-08-08-c-sigma-derivation-status.md` §"THE ONE ASSUMPTION BEING CARRIED"
**New probe:** `computations/probes/one_loop_prefactor_exponent_probe.py`

## What was asked

`c_σ = 2^{−3/4}` was upgraded to DERIVATION carrying exactly one stated
assumption:

```
c_σ  ∝  |τ|^{−1/2}
```

described as "the standard GGMW/Ohtsuki saddle-point form … validated here, not
proved", with the closing note that *"proving it for links is the real remaining
gap, and it is a research problem, not a computation."*

That framing is right about the gap and wrong about where it sits.

## Finding 1 — the exponent was never the assumed part

Every validation in this arc computes

```
k_c := c_σ · |τ|^{1/2}
```

and checks that `k_c` agrees across manifolds. That test looks like it holds the
exponent fixed and measures `k`. Algebraically it does both at once, because for
any **pair** of manifolds

```
k_i = k_j   ⟺   log c_i + ½ log τ_i = log c_j + ½ log τ_j
            ⟺   (log c_i − log c_j)/(log τ_i − log τ_j) = −½
            ⟺   p_ij = −½
```

`k`-constancy and `p = −1/2` are **the same statement** on a pair. So the
exponent was pinned, to 17 digits, by data already in the corpus — the
`k_1 = k_2` agreement (rel diff 4.5e−18) *is* the measurement `p_{4_1,L5a1} =
−1/2`. Nobody read it that way, and the ledger consequently lists as "assumed"
something the data determines.

The new probe reports this explicitly as a re-expression, **not** as fresh
confirmation, because counting it twice would be the error this note exists to
prevent.

### What is genuinely new: the four-point fit

Four manifolds have `c_σ` determined independently of `τ` — `4_1`, `L5a1`,
`L6a4` from colored-Jones asymptotics, and `5_2` from Ohtsuki's Theorem 1.1.
With `p` and `k` both free that is 4 points against 2 parameters, leaving **2
residual degrees of freedom** — a test that can fail, which no pairwise identity
can be:

```
p = −0.498296258234        (predicted exactly −1/2)
k =  0.706990301516        (predicted 2^{−1/2} = 0.707106781187)
rms residual in log c_σ = 3.0e−4
```

Pairwise, over ~1 decade of `|τ|`:

| pair | p | \|p + ½\| |
|---|---|---|
| 4_1 vs L5a1 | −0.500000000000000009 | 9.2e−18 |
| 4_1 vs 5_2 | −0.500000000222371784 | 2.2e−10 |
| 5_2 vs L5a1 | −0.499999999669222325 | 3.3e−10 |
| 4_1 vs L6a4 | −0.498433015714425735 | 1.6e−3 |
| 5_2 vs L6a4 | −0.498194915333422998 | 1.8e−3 |
| L5a1 vs L6a4 | −0.497989547409452082 | 2.0e−3 |

The whole residual is L6a4, whose own witness already flags an unresolved
normalisation+cusp offset and returns `p = 1.4993` against an exact `3/2`
elsewhere. It is not evidence against `p = −1/2`.

### So the ledger should read

The single line "the prefactor form is assumed" is **two** statements with
different status:

* **the exponent `−1/2`** — pinned by existing data; not an assumption;
* **that `c_σ` is a function of `τ` alone** — genuinely assumed, and the
  load-bearing part.

A law `c_σ = k·|τ|^p·f(M)` with `f` weakly varying fits four points as well as
`f ≡ 1` does. Nothing in the corpus excludes it. **That** is the open problem,
and it is a smaller and better-shaped target than "the prefactor form".

## Finding 2 — two registered references bear on this and are cited by no audit

A survey of the reference ledger turned up material the `c_σ` audits never
reach for. Reporting what the registrations say; **none of these PDFs was read
here**, and the corpus's own notes say several were never read at all.

### Ohtsuki–Takata 2015 — may already be the `c = 1` prefactor form

`content/schema/references.ts:170` (`ohtsuki-takata-2015`, Geom. Topol. 19
(2015) 853–952) is registered with this note:

> "The second coefficient of the Kashaev-invariant asymptotic expansion of a
> two-bridge knot is a constant multiple of the square root of the twisted
> Reidemeister torsion at the holonomy representation"

If that paraphrase is accurate, it is the prefactor form for two-bridge knots —
i.e. the `c = 1` leg is **theorem-backed**, not merely "validated on `4_1` to 17
digits". No `c_σ` audit cites it. All four (2026-08-02 ×2, 2026-08-07,
2026-08-08) say the form is standard-but-unproved and reach only for
Garoufalidis–Yoon, which proves a *different* statement (1-loop = adjoint
torsion).

**Two reasons not to bank it yet**, both from the corpus's own record:

1. The registration says `DOI follows the msp.org pattern, PDF not read
   in-sandbox`, and there is no Ohtsuki–Takata file in `uploads/`.
2. The paraphrase says *square root of the torsion* — `τ^{+1/2}` — while the
   form in use is `|τ|^{−1/2}`. That is a sign discrepancy in the exponent. It
   is very likely a torsion-vs-inverse-torsion normalisation convention, which
   is exactly the kind of thing this corpus has been bitten by before, and it
   cannot be waved through from a bibliography note.

**Action:** obtain the paper and check the exponent convention. If it holds, the
`c = 1` leg upgrades from validated to proved and the open problem narrows to
links alone.

### Pandey–Wong 2023 — a *link* theorem the later audits do not mention

`references.ts:158` (`pandey-wong-2023`, arXiv:2308.06643):

> "Proves the Dimofte–Garoufalidis 1-loop conjecture for fundamental shadow
> link complements — which include the Borromean rings"

Two Borromean probes (`borromean_jones_1loop_torsion.py:50`,
`borromean_nz_adjoint_torsion.py:82`) call the reading "theorem-backed" on this
basis. Yet `2026-08-07-one-loop-multicusp-derivation.md:157` and
`2026-08-08-c-sigma-derivation-status.md:102` both state flatly that no theorem
covers the link case, citing only Garoufalidis–Yoon.

These are reconcilable — Pandey–Wong would cover `τ_DG = τ_adj` for links, while
nothing covers `c_σ ∝ |τ|^{−1/2}` for links — and that is probably the right
reading. But **no file says so**, and one part of the corpus calling a link
result theorem-backed while another says no link theorem exists is precisely the
sibling-file contradiction this arc has hit three times already. It should be
stated once, explicitly, wherever "no theorem covers links" appears.
`2308.06643` is also not in `uploads/` and its registration came from the
Garoufalidis–Yoon bibliography rather than a read.

### DGLZ — downloaded, registered, and cited nowhere

`uploads/0903.2472v1.pdf`, Dimofte–Gukov–Lenells–Zagier, *Exact results for
perturbative Chern-Simons theory with complex gauge group*. Registered at
`references.bib:3975` with the note "1-loop / torsion identification from the
physics side."

That single bib entry is its **only occurrence in the repository**. It appears
in no audit, probe, bean, or Lean file. This is the canonical physics origin of
the `1/√torsion` one-loop term — the thing the audits gesture at when they say
"the standard GGMW/Ohtsuki saddle-point form" — and it is sitting unread in
`uploads/`.

**This is the cheapest available move on the open problem.** Before treating the
τ-alone dependence as a research problem, read the paper the form is
attributed to and find out what it actually derives and under what hypotheses.

## Recommended action, in cost order

1. **Read `uploads/0903.2472v1.pdf` (DGLZ).** Already local, never opened, and
   it is the stated origin of the form. Nothing else on this list is cheaper.
2. **Resolve the Ohtsuki–Takata exponent convention** (`τ^{+1/2}` vs
   `|τ|^{−1/2}`) and, if it holds, mark the `c = 1` leg theorem-backed.
3. **Reconcile Pandey–Wong** with the "no theorem covers links" line in the two
   audits that assert it — one sentence, in both places.
4. **Amend the assumption ledger** in `2026-08-08-c-sigma-derivation-status.md`
   to split exponent from functional dependence, per Finding 1. (Done in this
   change.)
5. Only then treat "does `c_σ` depend on `τ` alone" as the research problem. It
   may already be answered in (1).

## Scope

Finding 1 is a re-reading of existing numbers plus one new fit; it derives
nothing and adds no manifold. Finding 2 reports what registration notes say
about papers that **were not read** — including by the registrations' own
admission — and must not be cited as though the theorems had been checked.
