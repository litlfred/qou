"""
HeckeEngine.jl — Julia bindings for `hecke-engine` via the
`hecke-engine-c` C ABI.

Tier-3 wrapper per workplan v2 §3.6 — sibling of `pyhecke-native`,
`hecke-engine-{node,wasm,jvm,r,c,octave}`. The Julia community
(Oscar, Nemo, AbstractAlgebra) is a natural consumer for an
Iwahori-Hecke H_3(q) Gram / Markov-trace surface.

Build:
    cd ../hecke-engine-c
    cargo build --release

The Julia side discovers the resulting `libhecke_engine_c.{so,dylib,dll}`
via the `HECKE_ENGINE_C_LIB` env var, falling back to the conventional
location `../hecke-engine-c/target/release/`.

Usage:
    using HeckeEngine
    q0 = 1.10998
    z  = markov_z(q0)
    G  = gram_matrix(q0)
    d  = gram_det(q0)
"""
module HeckeEngine

using Libdl

# ── Library discovery ──
const _LIB = let
    env = get(ENV, "HECKE_ENGINE_C_LIB", "")
    if !isempty(env)
        env
    else
        # Convention: tools/hecke-engine-julia and tools/hecke-engine-c
        # are siblings. Walk up to the workspace root.
        root = dirname(dirname(@__DIR__))
        for ext in (".so", ".dylib", ".dll")
            cand = joinpath(root, "hecke-engine-c", "target", "release",
                            "libhecke_engine_c$ext")
            if isfile(cand)
                @goto found
            end
        end
        error("""
            HeckeEngine: could not find libhecke_engine_c.{so,dylib,dll}.

            Expected location: tools/hecke-engine-c/target/release/.
            Build it with:    cd tools/hecke-engine-c && cargo build --release

            Or set the HECKE_ENGINE_C_LIB env var to an explicit path.
            """)
        @label found
        cand
    end
end

# ── Public API ──

"""Engine version (matches the underlying hecke-engine-c crate)."""
function version()::String
    ptr = ccall((:qou_hecke_version, _LIB), Ptr{Cchar}, ())
    unsafe_string(ptr)
end

"""Markov parameter z = 1 / (q^{1/2} + q^{-1/2})."""
markov_z(q::Float64)::Float64 = ccall((:qou_hecke_markov_z, _LIB), Float64, (Float64,), q)

"""Hecke relation coefficient h = q − q⁻¹."""
hecke_h(q::Float64)::Float64 = ccall((:qou_hecke_h, _LIB), Float64, (Float64,), q)

"""Markov-trace weights on the NF basis (length-6 vector)."""
function trace_weights(q::Float64)::Vector{Float64}
    out = Vector{Float64}(undef, 6)
    ccall((:qou_hecke_trace_weights, _LIB), Cvoid,
          (Float64, Ptr{Float64}), q, out)
    out
end

"""Gram matrix G_ij = tr_M(b_i · b_j), 6×6 Julia matrix."""
function gram_matrix(q::Float64)::Matrix{Float64}
    flat = Vector{Float64}(undef, 36)
    ccall((:qou_hecke_gram_matrix_flat, _LIB), Cvoid,
          (Float64, Ptr{Float64}), q, flat)
    # Rust emits row-major; Julia matrices are column-major →
    # reshape with row-major layout, then transpose.
    transpose(reshape(flat, 6, 6))
end

"""Gram determinant."""
gram_det(q::Float64)::Float64 = ccall((:qou_hecke_gram_det, _LIB), Float64, (Float64,), q)

export version, markov_z, hecke_h, trace_weights, gram_matrix, gram_det

end # module
