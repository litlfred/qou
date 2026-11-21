**Algorithm (Gröbner–Shirshov length filtration).**
*Compute the length filtration on $H_n(q)$ and the length grade of
each normal form.*

### Input

- *Braid index $n$, substrate parameter $q$.*

### Output

- *Length-graded decomposition
  $H_n(q) = \bigoplus_{\ell \geq 0} F_\ell / F_{\ell - 1}$ where
  $F_\ell$ is the span of basis elements $T_w$ with $\ell(w) \leq \ell$.*
- *For each input word, the length grades of the basis elements
  $T_w$ in its normal form.*

### Algorithm

```
1. For each ℓ from 0 to ℓ_max:
     enumerate basis elements T_w with ℓ(w) = ℓ.
2. Build the associated graded ⊕_ℓ gr_ℓ H_n(q).
3. Reduce each input word to normal form and record the length
   grade of every basis element in it.
4. Return the filtration and the per-word grades.
```

### Correctness conditions

*The standard basis $\{T_w\}$ of $H_n(q)$ splits the length
filtration $F_\ell = \operatorname{span}\{T_w : \ell(w) \leq \ell\}$,
so every element has a unique decomposition by length grade, and
$F_a F_b \subseteq F_{a+b}$
([Length-filtration spectral sequence of the Hochschild complex of $H_n(R, q)$](#prop:gb-spectral-sequence), part 1).
No spectral-sequence collapse is used. None holds in general: for the
Hochschild complex of $H_3$ filtered by length, $d_2$ and $d_4$ are
nonzero.*

### Complexity

*$O(\dim H_n(q))$ basis enumeration, plus one normal-form
reduction per input word.*

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
records, for each test word, the normal form, its length grades and
the reduction log.*

### Notes

*Step 8 uses the splitting of the length filtration by the
standard basis; it does not need a spectral sequence.*
