# Where flavour SU(3) could live in QOU — and why neither candidate works

**Date:** 2026-08-03
**Branch:** `claude/eightfold-way-a2-lattice-ijoegv`
**Bean:** `qou-m5sd` (T3), epic `qou-8lxd`
**Trigger:** owner ruling that the eightfold-way blocker is singular — *"there
is no SU(3), and a proved theorem says it can't come from one fibre; it must
be groupoid-level."*

**Bottom line.** The canonical route from a Hecke algebra to $\mathrm{SU}(3)$
is **Schur–Weyl duality**, and the corpus already carries it. Running the
dimension battery before building anything (per
[`compute-author.md` §3.3](../../.claude/skills/local/compute-author.md))
finds **two** three-dimensional-looking objects in QOU, and shows that
**neither is the flavour-$\mathrm{SU}(3)$ fundamental** — each for a
different, citable reason. The open problem sharpens from *"SU(3) is open,
no construction"* to a single falsifiable requirement (§4).

## 1. Schur–Weyl is the right frame, and it is already here

Quantum Schur–Weyl duality makes $\mathcal U_q(\mathfrak{gl}_N)$ and
$\mathbf H_n(q)$ mutual centralizers on $V^{\otimes n}$:

$$
  V^{\otimes n} \;\cong\; \bigoplus_{\lambda \vdash n,\ \ell(\lambda)\le N}
    V_\lambda^{\mathfrak{gl}_N} \otimes S^\lambda_{\mathbf H_n(q)} .
$$

This is exactly "symmetry visible only at the groupoid level — multi-strand
structure … and the interaction of distinct fibres", because the group acts
on the **tensor power**, never inside one fibre. It is therefore fully
compatible with the proved $\mathrm{SU}(2)$-emergence theorem, and is the
natural place to look.

## 2. Correction to a claim made earlier this session

An earlier note in
[the dialog assessment](2026-08-03-eightfold-way-a2-q-deformation-dialog-assessment.md)
§T3 read: *"$\dim\mathbf H_3(q)=6$, blocks $1,2,1$ — there is no
$\mathbf 8\oplus\mathbf 1$ there."* Literally true, but **misleading**, and it
pointed at the wrong object. The Hecke blocks are the **multiplicity
spaces**, not the $\mathrm{SU}(3)$ irreps. At $N = 3$:

| $\lambda \vdash 3$ | $\dim V_\lambda^{\mathfrak{gl}_3}$ | Hecke mult $\dim S^\lambda$ |
|---|---|---|
| $(3)$ | **10** (decuplet) | 1 |
| $(2,1)$ | **8** (octet) | 2 |
| $(1^3)$ | **1** (singlet) | 1 |

$27 = 10\cdot 1 + 8\cdot 2 + 1\cdot 1 = 3^3$. ✓

So the eightfold way **is** precisely the Schur–Weyl partner of
$\mathbf H_3(q)$, and the Hecke block dimensions $(1,2,1)$ are exactly the
multiplicities of decuplet / octet / singlet. The right question was never
"where is the $\mathbf 8$" — it is **"why would $N = 3$?"**

## 3. Both candidate three-dimensional objects fail — for different reasons

### 3a. The $\mathfrak{gl}_3$ already in the corpus is a homonym

[`q-deformed-nuclear-models-comparison.md`](../../content/quantum-observable-universe/observations/q-deformed-nuclear-models-comparison.md)
states `prop:shell-schur-weyl-self-duality`: on $(\mathbb C^3)^{\otimes n}$
the mutual-centralizer pair is $\mathcal U_q(\mathfrak{gl}_3)\times
\mathbf H_n(q)$ — but it says in the same sentence that this
$\mathrm{SU}(3)$ is **Elliott's** $\mathrm{SU}(3)$, the nuclear
shell-model symmetry, recovered as the $q=1$ image. Elliott's
$\mathrm{SU}(3)$ acts on the **three spatial oscillator directions**, not on
$u/d/s$ flavour. Same three letters, different object.

This is the *same failure mode* flagged in the dialog assessment §4 for
`1803.04009` — a group-name homonym. It recurring twice in one session on the
same symbol is worth noting: **before claiming any $\mathrm{SU}(3)$ in this
corpus, state what it acts on.**

### 3b. The single-fibre tower is hard-capped at $N = 2$

[`why-b3.md`](../../content/quantum-observable-universe/braids-and-knots/why-b3.md):

> "The Descartes condition $\chi(A) = -6$ forces the gauge group to be a
> quantum form of $\mathrm{SU}(2)$, which has rank $2$. Consequently, the
> fundamental representation $V$ is $2$-dimensional."

and [`knot-eigenbasis-complete.md`](../../content/quantum-observable-universe/braids-and-knots/knot-eigenbasis-complete.md)
decomposes $V^{\otimes n}$ over "partitions of $n$ with **at most two
parts**". So the Schur–Weyl commutant of $\mathbf H_n(q)$ on QOU's own
$V^{\otimes n}$ is $\mathcal U_q(\mathfrak{gl}_2)$, and at $n=3$:

$$
  V^{\otimes 3} = 4\cdot 1 + 2\cdot 2 = 8 = 2^3 ,
  \qquad \lambda = (1^3) \ \textbf{drops entirely (3 rows > 2)} .
$$

The singlet-carrying block is not merely small — it is **absent**. No choice
of $q$ restores it: the row cap is $\dim V$, which the Descartes condition
fixes at 2.

### 3c. The colour three-object is icosahedral, not $\mathrm{SU}(3)$

`ColorPairIsotypicDecomposition` (bean `qou-ctkw`, used by
[`ColorFlavorIsospinSelection.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ColorFlavorIsospinSelection.lean))
carries a genuinely 3-dimensional object with

$$
  T_1 \otimes T_1 = A \oplus T_1 \oplus H,
  \qquad \mathrm{Sym}^2 = A \oplus H \ (\dim 6),
  \qquad \mathrm{Alt}^2 = T_1 \ (\dim 3).
$$

The dimensions $9 = 6+3$ look like $\mathbf 3\otimes\mathbf 3 = \mathbf 6_S
\oplus \bar{\mathbf 3}_A$. **They are not.** The discriminator:

| | $\mathrm{Sym}^2$ of the 3 | contains a singlet? |
|---|---|---|
| $\mathrm{SU}(3)$ | $\mathbf 6$, **irreducible** | **no** |
| $\mathrm{SO}(3)$ / icosahedral | $1 \oplus 5$ | **yes** |
| corpus $T_1$ | $A \oplus H = 1 \oplus 5$ | **yes** |

A singlet in $\mathrm{Sym}^2$ of the fundamental is an invariant **symmetric**
bilinear form. $\mathrm{SU}(3)$ has none — its fundamental is not
self-dual, and $\mathrm{Sym}^2(\mathbf 3) = \mathbf 6$ is irreducible. So the
colour $T_1$ carries an orthogonal/icosahedral symmetry, not
$\mathrm{SU}(3)$. (The labels $A, T_1, H$ with dimensions $1,3,5$ are
icosahedral irrep names, consistent with the framework's Bring / $S_5$ /
binary-icosahedral machinery — this is a *coherent* reading of that object,
just not a flavour-$\mathrm{SU}(3)$ one.)

**Scope.** §3b and §3c are **scope-(b) structural exclusions** with the
invariants named — the row-count cap $\ell(\lambda)\le\dim V$, and the
irreducibility of $\mathrm{Sym}^2(\mathbf 3)$ under $\mathrm{SU}(3)$. Neither
is a numerical near-miss that a better fit could rescue.

## 4. What the open problem now is, precisely

> **Flavour $\mathrm{SU}(3)$ requires a 3-dimensional object $W$ in the
> groupoid whose symmetric square $\mathrm{Sym}^2 W$ is irreducible (no
> invariant symmetric form), equivalently whose fundamental is not
> self-dual.**

> **⚠ CORRECTION (2026-08-04) — "QOU currently contains no such object" was
> wrong.** That sentence was written without completing the corpus-grep
> checklist (the octonion / $G_2$ path was not walked), and it is the exact
> failure mode `AGENTS.md` §"Before declaring open" warns about. The corpus
> **does** contain a non-self-dual triple:
> [`2026-07-12-octonion-recovery-from-genus4-analysis.md`](2026-07-12-octonion-recovery-from-genus4-analysis.md)
> §Investigation 2 records colour $\mathrm{SU}(3)\subset G_2 = \mathrm{Aut}(\mathbb O)$
> with the Günaydin–Gürsey decomposition
> $\mathbf 7 = \mathbf 1 \oplus \mathbf 3 \oplus \bar{\mathbf 3}$.
> The $\mathbf 3$ and $\bar{\mathbf 3}$ there are **complex conjugates, hence
> genuinely non-self-dual** — precisely what §4 demands. Its discrete
> skeleton is machine-checked (`det3_cyclic_invariant`: the associator is
> $\mathrm{GL}(3,\mathbb F_2)\cong \mathrm{PSL}(2,7)$-invariant, the
> Fano/Klein-quartic symmetry). What is missing is the **continuous** $G_2$
> completion — the coset $S^6 = G_2/\mathrm{SU}(3)$ — which is a **Mathlib
> gap** (no `Octonion`, no `G₂` Lie group), *not* a structural obstruction.
>
> Two caveats keep this honest: (i) that $\mathrm{SU}(3)$ is **colour**, not
> flavour — but colour $\mathrm{SU}(3)$ is exactly the item
> `sm-open-problems.md` lists as *"open: no construction; octonion fragments
> only"*, so it is the more valuable target anyway; (ii) $\mathrm{PSL}(2,7)$
> lives at genus 3 (Klein quartic) while QOU's substrate is genus 4 (Bring,
> $S_5$, icosahedral), and the audit reaches octonions only at the **lattice**
> level via $A_5\to E_8$ McKay, not as a product on $H^1$.
>
> §3a–§3c stand unchanged: the two objects examined there really are
> excluded. The corrected claim is narrower — *those* candidates fail, and a
> third, better one exists and is partly built.

That is a single, cheap, falsifiable test any future candidate must pass, and
it prunes in advance every construction built on a self-dual or orthogonal
triple. Three consequences worth stating:

1. **Do not look inside $V^{\otimes n}$ for one fibre.** §3b caps it at
   $\mathfrak{gl}_2$ structurally.
2. **Do not reuse the colour $T_1$.** §3c excludes it by the $\mathrm{Sym}^2$
   test.
3. **The remaining honest direction** is the one the corpus itself names and
   has not built: *interaction of distinct fibres* — a groupoid with
   inequivalent fibre objects, where the relevant representation is not a
   tensor power of one $V$. Whether such a $W$ exists with non-self-dual
   fundamental is untested, and is the actual content of T3.

## 5. Recommended next step

Formalize the test before searching: a Lean lemma stating that a
3-dimensional object with an invariant symmetric bilinear form cannot carry a
faithful $\mathrm{SU}(3)$ action (equivalently, $\mathrm{Sym}^2$ of the
$\mathrm{SU}(3)$ fundamental is irreducible). That is small, generic-ring
where possible, and converts §4 from prose into a machine-checkable gate
every future candidate must clear — the formalize-first prune applied to the
framework's single largest open item.

Arithmetic in §2/§3b verified by hook-content and hook-length formulas
(exact integer arithmetic, $N \in \{2,3\}$, $n \in \{2,3\}$; totals match
$N^n$ in every case).
