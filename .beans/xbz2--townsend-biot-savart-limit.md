# kappa_squared_tends_to_zero_axiom

The theorem `kappa_squared_tends_to_zero_axiom` in `townsend-biot-savart-strain.lean` requires an epsilon-delta proof of the limit of `|V2 / V1|` as `\tau \to 0`. 
Specifically it needs `\tau^2 \log \tau \to 0`, which is a standard real analysis fact but requires substantial setup using `Filter.Tendsto` and `Real.log` bounds.
