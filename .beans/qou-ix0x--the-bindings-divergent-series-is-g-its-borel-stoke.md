---
# qou-ix0x
title: The binding's divergent series is G, its Borel-Stokes plane is EMPTY, and the untried summation is the Habiro/cyclotomic one
status: todo
type: task
priority: normal
created_at: 2026-09-07T08:46:20Z
updated_at: 2026-09-07T08:46:20Z
---

Owner pointer, 2026-09-07: *"On A_infty there was a divergent series..."*, against the standing target *"ultimate target is to close gap in binding"*.

## Where the divergent series actually is

**NOT in `B(K)` for a fixed nucleus.** `conj:binding-manybody-eq-jet-filtration` writes `B(K) = Σ_{n≥2} B_n(K)` and `jet-filtration-binding-extensive` writes `B(A) = Σ_{n=2}^{A}`. These look like they disagree and **they do not**: a nucleus with `A` nucleons has no `n`-body term for `n > A`, so the sums are equal. Do not report this as an internal contradiction — I nearly did.

**It is `G(x;q) = Σ_n B_n x^n`**, the binding generating function, which is genuinely over all `n` and is the object carrying the q-difference equation. Two facts about it are already proved sorry-free:

- **`BindingGevreyHalf`** — `n! ≤ 4ⁿ I(n)² ≤ 8ⁿ n!`, so the lever-1 binding period is Gevrey-**1/2**. Divergent, and its divergence class is pinned.
- **`BindingScalarKernelParityExclusion`** — its q-difference module `L_K = (q²x−1)σ² − (q−1)σ − (q−1)` is irreducible of rank 2 and pure isoclinic of Newton slope 1/2.

## What I established this session, which closes the obvious use of that divergence

`QOU/Mass/BindingNoAlienPlane.lean` (sorry-free, lean-direct exit 0): **the divergence carries no Stokes data, on either plane.**

- classical: Gevrey-1/2 ⇒ level-1 Borel transform entire ⇒ no alien derivatives there.
- q: pure isoclinic ⇒ Ramis–Sauloy math/0611521 §2.2 verbatim, pure modules "are irregular objects **without wild monodromy**" ⇒ no q-alien derivations, no Stokes operators.

So the series diverges and the *resurgent* content of that divergence is empty.

## THE UNTRIED SUMMATION — this is the bean

Borel–Laplace is not the only way to sum a divergent q-series, and the corpus already uses the other one. **Habiro / cyclotomic summation** converges at every root of unity rather than along a ray, so purity — a statement about the slope filtration and the Stokes sheaf — says **nothing about it**.

The corpus already places the right objects there and this is prior art, not my idea:

- `full-pole-structure-mass-trace.md`: "The Markov trace of any closed braid lies **natively** within the Habiro cyclotomic completion" `\hat{ℤ[q]} = varprojlim ℤ[q]/(q;q)_n`.
- `z-Habiro ring`: `Φ_q(z) = Π(1−q^{-k}z)^{-1}` is "**ill-defined as a polynomial but exists as a formal limit within this completion**" — the exact move needed for a divergent all-orders object.
- `operator-selection-lp-interpretation.md` puts the LP's Markov traces and Gram entries in `\hat{ℤ[q]}` too.

And it is what the **owner's 2026-09-03 full-tower ruling** asks for: "all `n` of the Hecke tower *and* all orders in `q`". The Habiro ring is precisely the object holding all orders in `q` at once.

## Why this is not excluded by the b3 = 0 diagnosis

The 09-05 audit derives the model's `b3 = 0` from pair-locality (`b3_eq_zero_of_pairLocal`) and explains pair-locality by `HH^k(H_n(q), H_n(q)) = 0` at **generic** `q`. Both are level-wise statements at a fixed finite `n` and at a *generic* point. `H_n(q)` at a **root of unity** is NOT semisimple — `2026-06-04-kontsevich-soibelman` records this explicitly: cellular over `ℤ[q^{±1}]`, generic fibre semisimple, "the root-of-unity fibres are **non-semisimple**". A cyclotomic evaluation therefore lands exactly where the semisimplicity that forces `b3 = 0` fails.

## ROAST — what is wrong with this, stated by me

1. **It is a LOCATION, not a derivation.** It says where a nonzero 3-body datum could live. It does not compute `b3 = +1.4262 MeV`, and a completion is enormous. Do not write it up as progress on the number.
2. **The `A_∞` conflation I nearly committed.** `direct-limit-algebra-su2.md` defines `A_∞ = colim End(J^nO(SU(2))) ≅ U(𝔰𝔲(2))` — the SU(2) jet tower. The binding's "jet filtration" is a DIFFERENT object: `lem:bond-order-eq-jet-degree` uses the Gröbner–Shirshov Coxeter-length filtration on `H_{3A}(q)`. Both are called jet filtrations. Any argument routed through the SU(2) one is a symbol collision.
3. **`b3` is a glyph collision three ways.** A grep for `b3` in this corpus returns `B_3(ℂ)` (the Bloch group, in the α_EM fixed point), `b3ix` (the Q_β odd channel), and `B3` (a Gröbner monomial in `HeckeCompletion.lean`). None is the connected 3-body cumulant. Resolve before citing.
4. **The non-semisimplicity is at roots of unity; the substrate `q₀ ≈ 1.11` is not one.** So a cyclotomic route has to explain how root-of-unity data reaches an evaluation at a non-root-of-unity point. The Habiro ring's whole content is that it does — but that is the thing to establish, not to assume.
5. **Anti-fit gate.** Any number extracted from a cyclotomic evaluation and matched to `b3` without a derived map is a fit. `qou-brng` was already burned once by a coincidence of exactly this shape (the ≈ ℏ_q² saturated fraction, now recorded as "more likely numerology than a derived prediction").

## FIRST BRICK — cheap, no compute, falsifiable

Does the corpus's `b3 = 0` proof survive at a root of unity? `b3_eq_zero_of_pairLocal` derives `b3 = 0` from pair-locality as a **hypothesis**. So the question is not whether the theorem holds — it does — but whether **pair-locality itself** is derivable at a root of unity, where `HH^k ≠ 0`. If pair-locality is genuinely a generic-`q` fact, the theorem simply has no hypothesis to stand on there, and `b3` is unconstrained by it. That is a Lean-readable question about one hypothesis, needs no probe, and either answer is progress.

Companion: `qou-dk8a` (the global connection matrix, the other unexcluded route).
