% smoke.m — Octave smoke test for hecke-engine MEX bindings.
%
% Run from this directory:
%   octave --eval "addpath('..'); smoke"
%
% Mirrors test/smoke.test.js from hecke-engine-node + the Rust
% unit tests in hecke-engine-jvm.

q0 = 1.10998;  % substrate q_0

% 1. version
v = qou_hecke_version();
printf("hecke-engine %s\n", v);
assert(!isempty(v));

% 2. markov z (positive)
z = qou_hecke_markov_z(q0);
printf("z(q_0) = %.6f\n", z);
assert(z > 0, "markov_z must be positive");

% 3. hecke h (formula)
h = qou_hecke_h(q0);
expected = q0 - 1 / q0;
assert(abs(h - expected) < 1e-12, sprintf("h mismatch: got %.6f, expected %.6f", h, expected));

% 4. trace weights (length 6, [1, z, z, z^2, z^2, z^3])
w = qou_hecke_trace_weights(q0);
assert(numel(w) == 6, "trace_weights must have 6 elements");
assert(abs(w(1) - 1.0) < 1e-12);
assert(abs(w(2) - z) < 1e-12);
assert(abs(w(6) - z * z * z) < 1e-12);

% 5. Gram matrix (6x6)
G = qou_hecke_gram_matrix(q0);
assert(size(G, 1) == 6 && size(G, 2) == 6, "Gram must be 6x6");

% 6. Gram det (non-zero + finite; Gram at q_0 is indefinite so sign isn't constrained)
d = qou_hecke_gram_det(q0);
assert(isfinite(d), "gram_det non-finite");
assert(abs(d) > 1e-30, "gram_det too close to zero");

printf("OK: 6/6 smoke tests pass\n");
