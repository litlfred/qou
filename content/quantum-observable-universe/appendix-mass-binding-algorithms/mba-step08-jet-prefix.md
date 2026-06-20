**Algorithm (Jet-prefix transport, $q \to 1$ limit).**
*Truncate the Markov-trace Laurent polynomial at jet order $N$
and transport its leading coefficients to the archimedean fibre
at $q = q_0$ via the GS filtration of Step 7.*

### Input

- *Markov-trace polynomial $P_K(q) = \mathrm{tr}_M(\mathrm{NF}(K))$
  (output of Step 3, evaluated symbolically).*
- *Target jet order $N \in \mathbb{N}$ (chosen by precision goal —
  default $N = \lceil \log_{10}(1/\varepsilon) / 2.07 \rceil - 1$
  per AGENTS.md "𝔔_β c_k truncation order").*

### Output

- *Truncated polynomial
  $P_K^{(N)}(q) = \sum_{d = -N}^{N} c_d \, q^d$ with
  $|P_K(q) - P_K^{(N)}(q)| = O(h^{N+1})$ where $h = q - 1$.*

### Algorithm

```
1. Expand P_K(q) around q = 1 as a Taylor / Laurent series in h.
2. Retain terms up to order h^N.
3. Match length levels ℓ to jet orders d via the GS-filtration
   correspondence (`prop:jet-prefix-gb-filtration`).
4. Return the truncated polynomial with jet-order metadata.
```

### Correctness conditions

1. *[`prop:jet-prefix-gb-filtration`](#prop:jet-prefix-gb-filtration)
   gives the length $\leftrightarrow$ jet-order correspondence used in step 3.*
2. *[`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence) ($E_2$
   collapse, Step 7) ensures the truncation does not mix orders.*

### Complexity

*$O(N \cdot \dim H_n(q))$ — linear in the target jet order and
in the Hecke dimension.*

### Python API entry point

*Canonical compute is the script
[`computations/gb_filtration_jet_order_reader.py`](../../../computations/gb_filtration_jet_order_reader.py),
which reads the GS-filtered NF and emits the per-jet-order
truncation witness. The substrate's precision discipline (compute
at 65 dps, serialise at 50 dps) is configured by
[`qou_substrate.precision`](../../../tools/qou-substrate/python/qou_substrate/precision.py).*

### Witness contract

*Canonical witness:
[`gb-filtration-jet-order-reader.witness.json`](../../../computations/gb-filtration-jet-order-reader.witness.json).
Records the truncated polynomial, the jet-order metadata, and a
cross-check against the symbolic Taylor expansion.*

### Notes

*The jet-prefix truncation is the **gate** between symbolic
($q$-exact) compute and the archimedean evaluation at $q_0$. The
choice of $N$ is precision-driven; see the $c_k$ truncation
sidecar for the analogous truncation in the $\mathfrak{Q}_\beta$ ladder.*
