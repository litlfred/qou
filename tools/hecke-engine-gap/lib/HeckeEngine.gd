#############################################################################
##  HeckeEngine.gd — Declarations for the HeckeEngine GAP package.
##
##  The implementation file HeckeEngine.gi wires each declaration to a
##  C-extension function exported from the kernel module
##  src/HeckeEngine.c (which itself ccall-wraps libhecke_engine_c.so).

#############################################################################
##  <#GAPDoc Label="QOU_HeckeEngine_Version">
##  <ManSection>
##  <Func Name="QOU_HeckeEngine_Version" Arg=""/>
##  <Returns>a string</Returns>
##  <Description>
##  Engine version (matches the underlying hecke-engine-c crate).
##  </Description>
##  </ManSection>
##  <#/GAPDoc>
DeclareGlobalFunction( "QOU_HeckeEngine_Version" );

#############################################################################
##  <#GAPDoc Label="QOU_MarkovZ">
##  <ManSection>
##  <Func Name="QOU_MarkovZ" Arg="q"/>
##  <Returns>a double</Returns>
##  <Description>
##  Markov parameter z = 1 / (q^{1/2} + q^{-1/2}).
##  </Description>
##  </ManSection>
##  <#/GAPDoc>
DeclareGlobalFunction( "QOU_MarkovZ" );

#############################################################################
##  <#GAPDoc Label="QOU_HeckeH">
##  <ManSection>
##  <Func Name="QOU_HeckeH" Arg="q"/>
##  <Returns>a double</Returns>
##  <Description>
##  Hecke relation coefficient h = q - q^{-1}.
##  </Description>
##  </ManSection>
##  <#/GAPDoc>
DeclareGlobalFunction( "QOU_HeckeH" );

#############################################################################
##  <#GAPDoc Label="QOU_TraceWeights">
##  <ManSection>
##  <Func Name="QOU_TraceWeights" Arg="q"/>
##  <Returns>a list of 6 doubles</Returns>
##  <Description>
##  Markov-trace weights on the NF basis of <M>H_3(q)</M>.
##  Returns <C>[1, z, z, z^2, z^2, z^3]</C> where
##  <M>z = </M> <Ref Func="QOU_MarkovZ"/>(q).
##  </Description>
##  </ManSection>
##  <#/GAPDoc>
DeclareGlobalFunction( "QOU_TraceWeights" );

#############################################################################
##  <#GAPDoc Label="QOU_GramMatrix">
##  <ManSection>
##  <Func Name="QOU_GramMatrix" Arg="q"/>
##  <Returns>a 6x6 matrix of doubles</Returns>
##  <Description>
##  Gram matrix <M>G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)</M> in the
##  Hoefsmit normal-form basis of <M>H_3(q)</M>.
##  </Description>
##  </ManSection>
##  <#/GAPDoc>
DeclareGlobalFunction( "QOU_GramMatrix" );

#############################################################################
##  <#GAPDoc Label="QOU_GramDet">
##  <ManSection>
##  <Func Name="QOU_GramDet" Arg="q"/>
##  <Returns>a double</Returns>
##  <Description>
##  Determinant of <Ref Func="QOU_GramMatrix"/>(q).
##  At the substrate value <M>q_0 \approx 1.110</M> the Gram matrix is
##  indefinite, so the sign of the determinant is not constrained.
##  </Description>
##  </ManSection>
##  <#/GAPDoc>
DeclareGlobalFunction( "QOU_GramDet" );
