using Test
using HeckeEngine

const Q0 = 1.10998  # substrate q_0

@testset "HeckeEngine.jl smoke" begin
    @testset "version" begin
        v = version()
        @test !isempty(v)
    end

    @testset "markov_z positive" begin
        @test markov_z(Q0) > 0
    end

    @testset "hecke_h matches formula" begin
        h = hecke_h(Q0)
        @test isapprox(h, Q0 - 1 / Q0; atol = 1e-12)
    end

    @testset "trace_weights shape" begin
        # [1, z, z, z², z², z³] — NOT a probability distribution.
        w = trace_weights(Q0)
        @test length(w) == 6
        @test isapprox(w[1], 1.0; atol = 1e-12)
        z = markov_z(Q0)
        @test isapprox(w[2], z; atol = 1e-12)
        @test isapprox(w[6], z^3; atol = 1e-12)
    end

    @testset "gram_matrix is 6x6" begin
        G = gram_matrix(Q0)
        @test size(G) == (6, 6)
        for v in G
            @test isfinite(v)
        end
    end

    @testset "gram_det finite + non-zero" begin
        # Gram at q_0 is indefinite — det sign isn't constrained,
        # only its finiteness + non-degeneracy.
        d = gram_det(Q0)
        @test isfinite(d)
        @test abs(d) > 1e-30
    end
end
