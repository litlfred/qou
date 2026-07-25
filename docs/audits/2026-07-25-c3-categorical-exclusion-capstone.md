# Capstone: c₃'s bar-odd anchor-swing is non-categorical at real q₀ — the proved exclusion chain, and the "q₀ varies" reframing

**Date:** 2026-07-25 · **Ties together:** #4282 (`6ec9646a`), #4288 (`bead1614`),
#4293 (`178967b4`) · **Tier:** capstone (no new result — consolidates three merged
sorry-free proofs) · **Discipline:** scope-(a)/(b) as marked; no fit; nothing wired;
`conj:algebraic-geometric-dilog-equivalence` stays OPEN.

## The chain (all Lean sorry-free, verified lean-direct exit 0 on merge)

| # | Object | Result |
|---|---|---|
| #4282 (C1) | ι-odd antisym off-diagonal `ω(β,p,q)=β·p−β⁻¹·q` = the bar-odd home | **anchor-smooth** (4.56 ppm); B1.2/B1.3 searched ι-even objects on ω's zero locus (why they walled) |
| #4288 | boost-hyperbola sensitivity `sensitivity²=1+4/barOdd²` | amplification ρ≥N forces `barOdd²≤4/(N²−1)`; at q₀ ρ≤~10 ≪ c₃'s 3×10⁶. Excludes **all magnitude routes** (in-block maps + holonomy magnitude); swing 0.221 ppm |
| #4293 | NZ phase `S(r,φ)=(√3/2)r²·sin 2φ`, φ=arg(u) | phase is maximal-leverage & ⊥ magnitude (∂S/∂φ|₀=√3r²≠0), **but frozen at real q₀**: u=2 log q₀ real ⇒ arg(u)=0 ⇒ swing **exactly 0** |

**Conjunction:** every categorical/geometric DOF at **strictly real** q₀ is anchor-
smooth or frozen ⇒ c₃'s 3.47% swing is **non-categorical at real q₀** — a fibre-level
`ε=Im(q)≠0` effect realized through the `1/u³` ladder representation (#3636/#3654).
This is the proof-completed form of the 2026-07-12 wall-resolution capstone.

## The "q₀ varies" reframing (owner, 2026-07-25) — interpretation, not a new proof

The chain's antecedent is *"q₀ is strictly real."* The owner's physical reading:
**q₀ is our local, measured substrate value — a field that varies, generically
carrying Im(q)≠0.** Under that reading the chain does not refute a categorical
origin; it **sharpens** it:

- #4293 shows the phase channel is *maximal-leverage but frozen only because
  arg(u)=0 for real q₀.* A varying q₀ with Im(q)≠0 gives arg(u)≠0 and **unfreezes
  exactly this DOF.**
- So a nonzero c₃ swing is, by the chain, a **proof-by-contradiction that q₀ is not
  strictly real/constant** — the swing *measures* the imaginary/varying part rather
  than being an artifact of it.
- The "proton-pin vs muon-pin" difference is then two observables sampling q₀ at
  slightly different points of its variation; their difference measures Im(q).

**Honesty guardrail (STRICT).** "q₀ varies" must not become an unfalsifiable knob
(free Im(q) fits anything — the §"no seventh fit-based ansatz" trap). The WALL proof
is the guardrail: it pins *how much* Im(q) the swing demands, so any q₀-variation
model is **measured against** #4293's `∂S/∂φ`, not fitted per-observable. A derived
distribution/scale/cross-observable correlation for Im(q) would be a real result; an
anchor-inverted Im(q) is a fit and stays labelled one.

## Coordination consequence
The in-block module-map search (#4283: θ-descendant tower + cyclotomic level) is
**provably** anchor-smooth (C1) and magnitude-bounded (#4288), so it cannot carry the
swing regardless of dressing/row/level. The live target is not another in-block map —
it is the Im(q) / q₀-variation DOF (a reframed option-2 keystone). Recorded on #4283.
