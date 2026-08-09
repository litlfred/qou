---
# qou-j6il
title: 'TRAP (critical): installed pyhecke_native .so is STALE and returns convention C -- any producer run silently reintroduces C'
status: todo
type: task
created_at: 2026-08-09T22:00:28Z
updated_at: 2026-08-09T22:00:28Z
---


## The trap

```
$ python3 -c "import pyhecke_native as p; print(p.markov_z(1.1099785827513808075916690956107688798744991218736))"
0.4993203341836945          <-- convention C
```

but the Rust source it is supposedly built from says convention **D**:

```rust
/// z = q³/(q² + 1) — Markov closure parameter, **trace convention D**
#[inline]
pub fn markov_z(q: f64) -> f64 {
    q * q * q / (q * q + 1.0)
}
```
`tools/hecke-engine/src/gram.rs:75`

**The installed binary is stale.**

| | |
|---|---|
| installed `.so` built | **2026-08-08 11:30:19 UTC** |
| `b5f4cb5b9` "qou-wgta item 10: the Rust engine stack C -> D, all nine bindings" | **2026-08-09 13:18:31 UTC** |

The wheel predates the migration by ~26 hours. Source is D; the artifact
executing is C.

## Why this is the worst kind of defect in this excision

Every other convention-C site found so far is *visible* — a formula or a number
in a file, catchable by grep or by the `trace-convention` axis. This one is
invisible to all of them: the source reads correctly, the registry reads
correctly, the axis passes, and the binary silently returns C.

Worse, it turns the standard remediation into a **reintroduction vector**. The
instruction throughout this excision has been "never hand-edit witness numbers,
regenerate from the producer". Doing exactly that, right now, with this binary
installed, would stamp fresh convention-C numbers into witnesses and content —
carrying the authority of a producer run and a `deps_hash`.

`markov_z` is not incidental. Its own docstring: *"re-exported through all nine
language bindings (pyhecke-native, wasm, node, c, jvm, r, julia, gap, octave) and
drives `trace_weights` and the `v_std` quark-volume channel"*. So anything
downstream of `trace_weights` in the native path is affected.

## Actions

- [x] Diagnosed: stale artifact, not a source defect
- [ ] Rebuild `pyhecke-native` from the D source (`maturin build --release`;
      cargo and maturin are both present in the container)
- [ ] Verify `markov_z(q0) == 0.612688037146465252`, not `0.4993203341836945`
- [ ] **Only then** run any producer
- [ ] Check the other eight bindings for stale build artifacts — the migration
      commit touched all nine, so if the Python wheel was stale the others
      plausibly are too. wasm/node are the ones most likely to be shipped
      pre-built.
- [ ] Consider a guard: a startup assertion, or a test, that fails when
      `markov_z(q0)` does not match the registry's `z_at_q0` for convention D.
      A stale binary should be loud, not silent.

## The general lesson

A compiled artifact is a convention surface, and it is the only one where source
review cannot see the defect. The `trace-convention` axis walks `content/**`; the
registry validator walks `computations/`, `tools/`, `qou-mass/`. **Nothing checks
that a built artifact agrees with the source it claims to come from.** The guard
above is the cheap fix and it belongs in CI, not in a bean.
