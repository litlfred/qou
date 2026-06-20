# Optical fibre / 1D QOU — information-theory section

**Branch:** `claude/optical-fibre-1d-qou-2026-06-08`
**Started:** 2026-06-08
**Status:** WIP — workplan stub (PR opened first per AGENTS.md branch+PR policy)

## Owner request (verbatim intent)

> Second PR: a section in **information theory** on **optical fibres /
> 1D QOU**. What can we say here? What does a typical 1D silicon /
> optical-fibre system look like? Don't need the most advanced
> material — the **simplest** version of an optical fibre, even rigid.
>
> What is exactly happening in QOU when we put **information on a single
> fibre**? As I understand it, the fibres don't interact with each
> other because they have a natural **surface boundary** — we should
> model that. What's in the literature?

## Reading of the request

A "fibre" here is the **physical** optical fibre (a 1D waveguide that
carries information), NOT the categorical fibre functor τ. The section
belongs in the **information-theory** chapter
(`content/quantum-observable-universe/information-theory/`).

Core questions to answer in QOU terms:

1. **What is a 1D QOU system?** The full substrate is the categorical
   action on a 3-manifold; an optical fibre is a (1+1)D / linear
   reduction. What survives dimensional reduction to a line?
2. **Information on a single fibre.** Putting a bit/qubit on a fibre =
   threading a braid/knot down a 1D channel. Channel capacity in
   Hecke / Markov-trace terms.
3. **Surface boundary → non-interaction.** Why parallel fibres don't
   talk: each has a boundary (cladding / total internal reflection)
   that makes the braid closure self-contained. Model = a bounded
   propagation region whose boundary action isolates the channel.
4. **Simplest model.** A rigid, straight 1D waveguide: the trivial
   braid carrier; modes = strands; dispersion = q-deformation of the
   propagation eigenvalue.

## Workplan (refined as survey lands)

1. **Survey** the information-theory chapter + any existing 1D / fibre /
   surface-boundary / photon content. — *in progress (Explore agent)*
2. **Lit check**: standard simplest-optical-fibre model (step-index,
   single-mode), total internal reflection, channel capacity (Shannon),
   and any quantum-channel / anyonic-wire references. — *pending*
3. **Define** the 1D QOU channel object (braid carrier on a line +
   boundary action) — content block(s) in `information-theory/`.
4. **Surface-boundary non-interaction** — a proposition that parallel
   bounded channels have vanishing inter-channel Hecke coupling.
5. **Information capacity** of a single fibre in Markov-trace terms;
   connect to the existing partition-function / horizon blocks.
6. Connect to the **q-regime** picture (PR #1999 sibling): linear/
   optical-fibre systems as a limiting regime of the q phase diagram.

## Discipline notes (AGENTS.md)

- Distinguish **physical fibre** from **fibre functor τ** explicitly in
  prose (collision risk).
- Corpus-grep before declaring anything missing.
- Lit claims get bibliographic citations (`content/schema/references.ts`).
- Primary content links point to the `.md` sibling.

## Sibling coordination

PR #1999 (`claude/gallant-bohr-w9f6a6`) covers phase transitions + H₂O +
the q-regime/anyonic upper-bound discussion. The optical-fibre "linear
system" regime is the shared seam — coordinate so the q phase-diagram
treatment isn't duplicated.
