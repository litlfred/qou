**Algorithm (Gröbner–Shirshov filtration with $E_2$ collapse).**
*Compute the length-graded filtration on $H_n(q)$ and assert
$E_2$-collapse of the associated spectral sequence — every higher
differential $d_r$ ($r \geq 2$) vanishes.*

### Input

- *Braid index $n$, substrate parameter $q$.*

### Output

- *Length-graded decomposition
  $H_n(q) = \bigoplus_{\ell \geq 0} F_\ell / F_{\ell - 1}$ where
  $F_\ell$ is the span of basis elements $T_w$ with $\ell(w) \leq \ell$.*
- *Boolean assertion that $d_r = 0$ for all $r \geq 2$ (i.e. the
  spectral sequence collapses at the $E_2$ page).*

### Algorithm

```
1. For each ℓ from 0 to ℓ_max:
     enumerate basis elements T_w with ℓ(w) = ℓ.
2. Build the associated graded ⊕_ℓ gr_ℓ H_n(q).
3. Verify d_2 = 0 by checking that the Markov trace pairs
   gr_ℓ with gr_{ℓ + r} trivially for r > 0.
4. Return the filtration and the collapse certificate.
```

### Correctness conditions

*[`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence)
asserts $E_2$-collapse for the GS filtration on $H_n(q)$ in the
QOU rigid-monoidal setting. The proof uses the diamond-lemma /
Gröbner basis structure of the Hecke relations and is standard
modulo the QOU-specific Markov coefficient $z$.*

### Complexity

*$O(\dim H_n(q))$ basis enumeration. The collapse check is
quadratic in the number of basis elements but the result is
cached per $(n, q)$ pair.*

### Python API entry point

*Canonical compute is the script
[`computations/gb_filtration_jet_tracker.py`](../../../computations/gb_filtration_jet_tracker.py);
run it directly to emit the witness. The Rust implementation
lives in [`tools/hecke-engine/`](../../../tools/hecke-engine/),
called via `pyhecke_native` when the per-particle builders need
the filtered NF.*

### Witness contract

*Canonical witness:
[`gb-filtration-jet-order.witness.json`](../../../computations/gb-filtration-jet-order.witness.json)
records the per-level filtration dimensions and the $d_2 = 0$
certificate.*

### Notes

*$E_2$-collapse is what justifies treating the GS filtration as
**exact**: any higher differential would re-mix length levels and
break the jet-order matching used by Step 8.*
