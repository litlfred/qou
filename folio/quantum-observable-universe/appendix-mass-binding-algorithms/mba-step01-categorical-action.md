**Algorithm (Categorical action of the braid group).**
*Construct the representation
$\rho_n\colon B_n \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$
that sends each braid generator $\sigma_i$ to a categorical
endomorphism of the $n$-fold monoidal product
$V^{\otimes n}$ in $\mathbf{C}$.*

### Input

- *Braid word $w = \sigma_{i_1}^{\varepsilon_1} \cdots \sigma_{i_k}^{\varepsilon_k}$ in $B_n$.*
- *Underlying rigid monoidal category $\mathbf{C}$ with chosen
  generating object $V \in \mathbf{C}$.*

### Output

- *Endomorphism $\rho_n(w) \in \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$
  as a finite composition of categorical generators
  (braiding $c_{V,V}$, dualities $\mathrm{ev}_V$, $\mathrm{coev}_V$,
  associator, unit).*

### Algorithm

```
1. For each generator σ_i in w:
     interpret σ_i as id^{i-1} ⊗ c_{V,V} ⊗ id^{n-i-1}
     where c_{V,V} is the braiding of C at (V, V).
2. For σ_i^{-1}: use c_{V,V}^{-1} = c_{V,V}^* (left-rigid dual).
3. Compose in order along w; the result is ρ_n(w).
```

### Correctness conditions

*Correctness rests on three upstream results.*

1. *The categorical action is **well-defined** by
   [Categorical action](#def:categorical-action) — the
   braiding $c_{V,V}$ in a rigid monoidal category satisfies the
   braid (Yang–Baxter) relations on $V^{\otimes n}$ by naturality
   of the hexagon axioms.*
2. *It **exists** under the QOU rigid-monoidal premise by
   [Existence of the categorical action](#prop:categorical-action-exists).*
3. *It is **unique** up to natural isomorphism by
   [Uniqueness of the categorical action (given $\Phi$)](#prop:categorical-action-unique).*

### Complexity

*$O(k)$ categorical morphisms for $|w| = k$. The endomorphism is
stored implicitly as a braid word until passed to the next step
(GS reduction), so the representation is **lazy** — no matrix
exponentiation occurs at this layer.*

### Python / Rust API entry point

*No standalone Python entry point — the categorical action is the
upstream specification, realised implicitly inside the Rust
`hecke-engine` crate at [`tools/hecke-engine/src/lib.rs`](../../../tools/hecke-engine/src/lib.rs).
Per-particle braid words are constructed via
`pyhecke.build_nucleon_nf` / `pyhecke.build_atom_nf` and consumed
by Step 2 (GS reduction).*

### Witness contract

*No standalone witness JSON: correctness is checked structurally
(braid relations are obeyed by the Hecke-relation specialisation
in Step 2). Property tests live in `tools/hecke-engine/tests/`.*

### Notes

*The categorical action is **fibre-independent**. It depends strictly on the rigid-monoidal structure of $\mathbf{C}$, independent of the fibre functor $\tau$. Archimedean specialisation enters at Step 9 (the nucleon mass ratio) via Markov trace evaluation at $q_0$.*
