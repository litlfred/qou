---
author:
- litlfred
bibliography:
- references.bib
date: 2026-04-01
title: QOU Visualizer
---

<div class="center">

  
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose,  
provided appropriate credit is given, a link to the license is provided,  
and any changes made are indicated.

</div>

**Proof-status key**

|                                               |                           |                                                   |                              |
|:---------------------------------------------:|:--------------------------|:-------------------------------------------------:|:-----------------------------|
|   <span style="color: ForestGreen"></span>    | Fully proved (sorry-free) | <span style="color: BurntOrange">$\forall$</span> | Stated in Lean (has `sorry`) |
| <span style="color: OliveGreen">-0.3em</span> | Merged into Mathlib       |   <span style="color: BrickRed">$\times$</span>   | Not ready to formalize       |

# Overview

## Introduction

The QOU Visualizer provides interactive views of the mathematical structures described in the Quantum Observable Universe paper. Rather than duplicating content, it references definitions and theorems from the main paper via cross-references and renders them through specialized visualization modes:

- **Bring’s surface** — quaternionic spectral resolvents rendered as 3D surfaces, with controls for the torsion parameter $q$, projection mode, and camera orbit.

- **Knot complements** — hyperbolic 3-manifold computations via the SnapPea kernel (compiled to WebAssembly), providing volumes, Dehn fillings, fundamental group presentations, and homology for knot complements in the particle registry.

- **Dependency graph** — the content-object DAG, showing how definitions, theorems, and conjectures depend on each other, with formalization status overlaid from the Lean build.

## Bring’s Surface

<div id="def:viz-brings-surface" class="definition">

**Definition 1.1** (Bring’s surface viewport). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.BringsSurface.ViewportState) The Bring’s surface visualizer renders quaternionic spectral resolvents as interactive 3D surfaces. The viewport state is fully serialisable (see `VizState` in `schemas/qou-types.ts`) and can be embedded in URLs or Markdown to reproduce a specific view.*

***Viewport parameters:***

- *$q$ — torsion/chirality parameter. $q = 0$ is classical; $q > 0$ introduces chiral twist in the colour-sector coordinates $(\mathfrak{r}, \mathfrak{g}, \mathfrak{b})$.*

- ***Mode** — `CP1` shows the $\mathbb{C}P^1$ exceptional fibre; `cone` shows the outgoing chiral tube cones.*

- ***Camera** — spherical coordinates $(\theta, \phi, r)$ with configurable look-at target.*

*$$\rho(s) = s \cdot \ell_P \cdot \sigma \cdot \Xi_q, \qquad
\psi_i(s) = \frac{2\pi i}{3} + q \cdot 2\pi s \cdot Q \cdot \gamma$$*

</div>

## Knot Complements

<div id="def:viz-knot-complement" class="definition">

**Definition 1.2** (Knot complement (SnapPea)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.KnotComplement) A **knot complement** $S^3 \setminus K$ is the 3-manifold obtained by removing a tubular neighbourhood of a knot $K$ from the 3-sphere. When $K$ is hyperbolic, the complement admits a unique complete hyperbolic structure (by Mostow rigidity), and its volume is a topological invariant.*

*The SnapPea kernel (`@snappea/kernel`, compiled to WebAssembly) computes:*

- ***Hyperbolic volume** via ideal triangulations*

- ***Dehn filling** coefficients $(m, l)$ on cusps*

- ***Fundamental group** presentations $\pi_1(S^3 \setminus K)$*

- ***Homology** $H_1(S^3 \setminus K; \mathbb{Z})$ via Smith normal form*

- ***Chern–Simons invariant** (when defined)*

- ***Canonical form** for isometry detection*

*In the QOU particle registry, each knot $K$ (indexed by Alexander–Briggs notation) corresponds to a particle, with the hyperbolic volume encoding the particle’s mass scale.*

</div>
