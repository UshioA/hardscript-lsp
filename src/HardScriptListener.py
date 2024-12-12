# Generated from ./src/HardScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HardScriptParser import HardScriptParser
else:
    from HardScriptParser import HardScriptParser

# This class defines a complete listener for a parse tree produced by HardScriptParser.
class HardScriptListener(ParseTreeListener):

    # Enter a parse tree produced by HardScriptParser#design.
    def enterDesign(self, ctx:HardScriptParser.DesignContext):
        pass

    # Exit a parse tree produced by HardScriptParser#design.
    def exitDesign(self, ctx:HardScriptParser.DesignContext):
        pass


    # Enter a parse tree produced by HardScriptParser#component.
    def enterComponent(self, ctx:HardScriptParser.ComponentContext):
        pass

    # Exit a parse tree produced by HardScriptParser#component.
    def exitComponent(self, ctx:HardScriptParser.ComponentContext):
        pass


    # Enter a parse tree produced by HardScriptParser#component_type.
    def enterComponent_type(self, ctx:HardScriptParser.Component_typeContext):
        pass

    # Exit a parse tree produced by HardScriptParser#component_type.
    def exitComponent_type(self, ctx:HardScriptParser.Component_typeContext):
        pass


    # Enter a parse tree produced by HardScriptParser#attributes.
    def enterAttributes(self, ctx:HardScriptParser.AttributesContext):
        pass

    # Exit a parse tree produced by HardScriptParser#attributes.
    def exitAttributes(self, ctx:HardScriptParser.AttributesContext):
        pass


    # Enter a parse tree produced by HardScriptParser#BindingStatement.
    def enterBindingStatement(self, ctx:HardScriptParser.BindingStatementContext):
        pass

    # Exit a parse tree produced by HardScriptParser#BindingStatement.
    def exitBindingStatement(self, ctx:HardScriptParser.BindingStatementContext):
        pass


    # Enter a parse tree produced by HardScriptParser#DataInstantiation.
    def enterDataInstantiation(self, ctx:HardScriptParser.DataInstantiationContext):
        pass

    # Exit a parse tree produced by HardScriptParser#DataInstantiation.
    def exitDataInstantiation(self, ctx:HardScriptParser.DataInstantiationContext):
        pass


    # Enter a parse tree produced by HardScriptParser#MixedInstantiation.
    def enterMixedInstantiation(self, ctx:HardScriptParser.MixedInstantiationContext):
        pass

    # Exit a parse tree produced by HardScriptParser#MixedInstantiation.
    def exitMixedInstantiation(self, ctx:HardScriptParser.MixedInstantiationContext):
        pass


    # Enter a parse tree produced by HardScriptParser#ComponentInstantiation.
    def enterComponentInstantiation(self, ctx:HardScriptParser.ComponentInstantiationContext):
        pass

    # Exit a parse tree produced by HardScriptParser#ComponentInstantiation.
    def exitComponentInstantiation(self, ctx:HardScriptParser.ComponentInstantiationContext):
        pass


    # Enter a parse tree produced by HardScriptParser#Loop.
    def enterLoop(self, ctx:HardScriptParser.LoopContext):
        pass

    # Exit a parse tree produced by HardScriptParser#Loop.
    def exitLoop(self, ctx:HardScriptParser.LoopContext):
        pass


    # Enter a parse tree produced by HardScriptParser#explicit_data_element.
    def enterExplicit_data_element(self, ctx:HardScriptParser.Explicit_data_elementContext):
        pass

    # Exit a parse tree produced by HardScriptParser#explicit_data_element.
    def exitExplicit_data_element(self, ctx:HardScriptParser.Explicit_data_elementContext):
        pass


    # Enter a parse tree produced by HardScriptParser#primary_symbol_list.
    def enterPrimary_symbol_list(self, ctx:HardScriptParser.Primary_symbol_listContext):
        pass

    # Exit a parse tree produced by HardScriptParser#primary_symbol_list.
    def exitPrimary_symbol_list(self, ctx:HardScriptParser.Primary_symbol_listContext):
        pass


    # Enter a parse tree produced by HardScriptParser#AccessExpr.
    def enterAccessExpr(self, ctx:HardScriptParser.AccessExprContext):
        pass

    # Exit a parse tree produced by HardScriptParser#AccessExpr.
    def exitAccessExpr(self, ctx:HardScriptParser.AccessExprContext):
        pass


    # Enter a parse tree produced by HardScriptParser#NumberExpr.
    def enterNumberExpr(self, ctx:HardScriptParser.NumberExprContext):
        pass

    # Exit a parse tree produced by HardScriptParser#NumberExpr.
    def exitNumberExpr(self, ctx:HardScriptParser.NumberExprContext):
        pass


    # Enter a parse tree produced by HardScriptParser#BinaryExpr.
    def enterBinaryExpr(self, ctx:HardScriptParser.BinaryExprContext):
        pass

    # Exit a parse tree produced by HardScriptParser#BinaryExpr.
    def exitBinaryExpr(self, ctx:HardScriptParser.BinaryExprContext):
        pass


    # Enter a parse tree produced by HardScriptParser#SymbolExpr.
    def enterSymbolExpr(self, ctx:HardScriptParser.SymbolExprContext):
        pass

    # Exit a parse tree produced by HardScriptParser#SymbolExpr.
    def exitSymbolExpr(self, ctx:HardScriptParser.SymbolExprContext):
        pass


    # Enter a parse tree produced by HardScriptParser#ListExpr.
    def enterListExpr(self, ctx:HardScriptParser.ListExprContext):
        pass

    # Exit a parse tree produced by HardScriptParser#ListExpr.
    def exitListExpr(self, ctx:HardScriptParser.ListExprContext):
        pass


    # Enter a parse tree produced by HardScriptParser#FieldExpr.
    def enterFieldExpr(self, ctx:HardScriptParser.FieldExprContext):
        pass

    # Exit a parse tree produced by HardScriptParser#FieldExpr.
    def exitFieldExpr(self, ctx:HardScriptParser.FieldExprContext):
        pass


    # Enter a parse tree produced by HardScriptParser#ConditionalExpr.
    def enterConditionalExpr(self, ctx:HardScriptParser.ConditionalExprContext):
        pass

    # Exit a parse tree produced by HardScriptParser#ConditionalExpr.
    def exitConditionalExpr(self, ctx:HardScriptParser.ConditionalExprContext):
        pass


    # Enter a parse tree produced by HardScriptParser#ParenExpr.
    def enterParenExpr(self, ctx:HardScriptParser.ParenExprContext):
        pass

    # Exit a parse tree produced by HardScriptParser#ParenExpr.
    def exitParenExpr(self, ctx:HardScriptParser.ParenExprContext):
        pass


    # Enter a parse tree produced by HardScriptParser#UnaryExpr.
    def enterUnaryExpr(self, ctx:HardScriptParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by HardScriptParser#UnaryExpr.
    def exitUnaryExpr(self, ctx:HardScriptParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by HardScriptParser#BitSelector.
    def enterBitSelector(self, ctx:HardScriptParser.BitSelectorContext):
        pass

    # Exit a parse tree produced by HardScriptParser#BitSelector.
    def exitBitSelector(self, ctx:HardScriptParser.BitSelectorContext):
        pass


    # Enter a parse tree produced by HardScriptParser#PartSelector.
    def enterPartSelector(self, ctx:HardScriptParser.PartSelectorContext):
        pass

    # Exit a parse tree produced by HardScriptParser#PartSelector.
    def exitPartSelector(self, ctx:HardScriptParser.PartSelectorContext):
        pass


    # Enter a parse tree produced by HardScriptParser#CommonList.
    def enterCommonList(self, ctx:HardScriptParser.CommonListContext):
        pass

    # Exit a parse tree produced by HardScriptParser#CommonList.
    def exitCommonList(self, ctx:HardScriptParser.CommonListContext):
        pass


    # Enter a parse tree produced by HardScriptParser#RangeList.
    def enterRangeList(self, ctx:HardScriptParser.RangeListContext):
        pass

    # Exit a parse tree produced by HardScriptParser#RangeList.
    def exitRangeList(self, ctx:HardScriptParser.RangeListContext):
        pass


    # Enter a parse tree produced by HardScriptParser#ListComprehension.
    def enterListComprehension(self, ctx:HardScriptParser.ListComprehensionContext):
        pass

    # Exit a parse tree produced by HardScriptParser#ListComprehension.
    def exitListComprehension(self, ctx:HardScriptParser.ListComprehensionContext):
        pass


    # Enter a parse tree produced by HardScriptParser#EmptyList.
    def enterEmptyList(self, ctx:HardScriptParser.EmptyListContext):
        pass

    # Exit a parse tree produced by HardScriptParser#EmptyList.
    def exitEmptyList(self, ctx:HardScriptParser.EmptyListContext):
        pass


    # Enter a parse tree produced by HardScriptParser#Generator.
    def enterGenerator(self, ctx:HardScriptParser.GeneratorContext):
        pass

    # Exit a parse tree produced by HardScriptParser#Generator.
    def exitGenerator(self, ctx:HardScriptParser.GeneratorContext):
        pass


    # Enter a parse tree produced by HardScriptParser#Filter.
    def enterFilter(self, ctx:HardScriptParser.FilterContext):
        pass

    # Exit a parse tree produced by HardScriptParser#Filter.
    def exitFilter(self, ctx:HardScriptParser.FilterContext):
        pass


    # Enter a parse tree produced by HardScriptParser#LocalBinding.
    def enterLocalBinding(self, ctx:HardScriptParser.LocalBindingContext):
        pass

    # Exit a parse tree produced by HardScriptParser#LocalBinding.
    def exitLocalBinding(self, ctx:HardScriptParser.LocalBindingContext):
        pass


    # Enter a parse tree produced by HardScriptParser#iterator.
    def enterIterator(self, ctx:HardScriptParser.IteratorContext):
        pass

    # Exit a parse tree produced by HardScriptParser#iterator.
    def exitIterator(self, ctx:HardScriptParser.IteratorContext):
        pass


    # Enter a parse tree produced by HardScriptParser#binding.
    def enterBinding(self, ctx:HardScriptParser.BindingContext):
        pass

    # Exit a parse tree produced by HardScriptParser#binding.
    def exitBinding(self, ctx:HardScriptParser.BindingContext):
        pass


    # Enter a parse tree produced by HardScriptParser#ParamSymbol.
    def enterParamSymbol(self, ctx:HardScriptParser.ParamSymbolContext):
        pass

    # Exit a parse tree produced by HardScriptParser#ParamSymbol.
    def exitParamSymbol(self, ctx:HardScriptParser.ParamSymbolContext):
        pass


    # Enter a parse tree produced by HardScriptParser#PrimarySymbol.
    def enterPrimarySymbol(self, ctx:HardScriptParser.PrimarySymbolContext):
        pass

    # Exit a parse tree produced by HardScriptParser#PrimarySymbol.
    def exitPrimarySymbol(self, ctx:HardScriptParser.PrimarySymbolContext):
        pass


    # Enter a parse tree produced by HardScriptParser#Identifier.
    def enterIdentifier(self, ctx:HardScriptParser.IdentifierContext):
        pass

    # Exit a parse tree produced by HardScriptParser#Identifier.
    def exitIdentifier(self, ctx:HardScriptParser.IdentifierContext):
        pass


    # Enter a parse tree produced by HardScriptParser#Interpolated.
    def enterInterpolated(self, ctx:HardScriptParser.InterpolatedContext):
        pass

    # Exit a parse tree produced by HardScriptParser#Interpolated.
    def exitInterpolated(self, ctx:HardScriptParser.InterpolatedContext):
        pass


    # Enter a parse tree produced by HardScriptParser#param_symbol.
    def enterParam_symbol(self, ctx:HardScriptParser.Param_symbolContext):
        pass

    # Exit a parse tree produced by HardScriptParser#param_symbol.
    def exitParam_symbol(self, ctx:HardScriptParser.Param_symbolContext):
        pass


    # Enter a parse tree produced by HardScriptParser#interpolation.
    def enterInterpolation(self, ctx:HardScriptParser.InterpolationContext):
        pass

    # Exit a parse tree produced by HardScriptParser#interpolation.
    def exitInterpolation(self, ctx:HardScriptParser.InterpolationContext):
        pass


    # Enter a parse tree produced by HardScriptParser#IntNumber.
    def enterIntNumber(self, ctx:HardScriptParser.IntNumberContext):
        pass

    # Exit a parse tree produced by HardScriptParser#IntNumber.
    def exitIntNumber(self, ctx:HardScriptParser.IntNumberContext):
        pass


    # Enter a parse tree produced by HardScriptParser#BoolNumber.
    def enterBoolNumber(self, ctx:HardScriptParser.BoolNumberContext):
        pass

    # Exit a parse tree produced by HardScriptParser#BoolNumber.
    def exitBoolNumber(self, ctx:HardScriptParser.BoolNumberContext):
        pass


    # Enter a parse tree produced by HardScriptParser#BitVectorNumber.
    def enterBitVectorNumber(self, ctx:HardScriptParser.BitVectorNumberContext):
        pass

    # Exit a parse tree produced by HardScriptParser#BitVectorNumber.
    def exitBitVectorNumber(self, ctx:HardScriptParser.BitVectorNumberContext):
        pass



del HardScriptParser