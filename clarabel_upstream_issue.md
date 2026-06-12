# Title: Feature Offer: Native Pure-Rust Arbitrary-Precision (MpfrFloat) and Symbolic (RationalReal) SDP Support

## Description
Hi Clarabel team!

We've been using Clarabel heavily for solving high-precision mathematical constraints and ran into the standard precision limits of `f64`. We recently built out **full support for arbitrary-precision (`MpfrFloat`) and exact rational (`RationalReal`) SDP solving natively in Rust** directly on top of the Clarabel architecture.

We accomplished this without introducing Fortran or BLAS/LAPACK C dependencies. We would love to contribute this upstream to the Clarabel.rs repository if you are interested!

### Technical Details & Architecture

1. **`FloatT` and Memory Arenas (`Copy` bypass):**
   - We observed that Clarabel's architecture assumes variables implementing `FloatT` are trivially copyable (i.e. `T: Copy`), which makes integrating `rug::Float` or `num_rational::BigRational` problematic due to heap allocations.
   - To solve this without refactoring Clarabel to use `.clone()` everywhere, we mapped the scalar primitives to a fast 4-byte `u32` thread-local handle. The `u32` acts as an index into a global per-thread memory arena (`RefCell<Vec<rug::Float>>`), making `MpfrFloat` perfectly `Copy`-compliant!
   - Math operations (`Add`, `Sub`, etc.) simply compute the underlying arithmetic and push the newly allocated result back onto the arena, returning the new integer handle.
   
2. **Native Pure-Rust LAPACK / BLAS:**
   - To make the SDP solver fully functional without OpenBLAS, we implemented the necessary core Level 2/3 BLAS matrix routines natively in pure Rust.
   - Includes standard Cholesky decomposition (`potrf`, `potrs`) and native matrix multiplications (`gemv`, `syrk`, `syr2k`).
   - We also successfully wrote a custom pure-Rust **Jacobi Eigensolver (`syevr`)** capable of accurately evaluating symmetric eigenvalue problems directly on arbitrary precision data types.

### Testing & Validation
We have expanded and validated the `mpfr_sdp_regression` test suite using the arbitrary precision backend to solve identical `f64` problems. The native Jacobi eigensolver decomposes the models accurately at 50+ digits of precision using the pure-Rust path!

We've done all the heavy lifting and validated it against our intensive constraint tasks. If you'd be open to reviewing a PR, we'd love to upstream these features so other teams can use Clarabel for arbitrary precision or exact-symbolic mathematical optimization.

Let us know your thoughts!
