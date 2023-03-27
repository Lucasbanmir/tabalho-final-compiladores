# Generated from C:/Users/lucas/Documents/trabalho final compiladores\trabalhoFinal_lucas.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .trabalhoFinal_lucasParser import trabalhoFinal_lucasParser
else:
    from trabalhoFinal_lucasParser import trabalhoFinal_lucasParser

# This class defines a complete generic visitor for a parse tree produced by trabalhoFinal_lucasParser.

class trabalhoFinal_lucasVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by trabalhoFinal_lucasParser#prog.
    def visitProg(self, ctx:trabalhoFinal_lucasParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#decVar.
    def visitDecVar(self, ctx:trabalhoFinal_lucasParser.DecVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#decConst.
    def visitDecConst(self, ctx:trabalhoFinal_lucasParser.DecConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#tipo.
    def visitTipo(self, ctx:trabalhoFinal_lucasParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#listaIds.
    def visitListaIds(self, ctx:trabalhoFinal_lucasParser.ListaIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#listaAtrib.
    def visitListaAtrib(self, ctx:trabalhoFinal_lucasParser.ListaAtribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#atrib.
    def visitAtrib(self, ctx:trabalhoFinal_lucasParser.AtribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#funcBloco.
    def visitFuncBloco(self, ctx:trabalhoFinal_lucasParser.FuncBlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#decFuncao.
    def visitDecFuncao(self, ctx:trabalhoFinal_lucasParser.DecFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#main.
    def visitMain(self, ctx:trabalhoFinal_lucasParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#comandos.
    def visitComandos(self, ctx:trabalhoFinal_lucasParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#comandosLoop.
    def visitComandosLoop(self, ctx:trabalhoFinal_lucasParser.ComandosLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#break.
    def visitBreak(self, ctx:trabalhoFinal_lucasParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#decPrint.
    def visitDecPrint(self, ctx:trabalhoFinal_lucasParser.DecPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#decInput.
    def visitDecInput(self, ctx:trabalhoFinal_lucasParser.DecInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#for.
    def visitFor(self, ctx:trabalhoFinal_lucasParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#while.
    def visitWhile(self, ctx:trabalhoFinal_lucasParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#return.
    def visitReturn(self, ctx:trabalhoFinal_lucasParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#decAtrib.
    def visitDecAtrib(self, ctx:trabalhoFinal_lucasParser.DecAtribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#callFunc.
    def visitCallFunc(self, ctx:trabalhoFinal_lucasParser.CallFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#orOp.
    def visitOrOp(self, ctx:trabalhoFinal_lucasParser.OrOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#passTermo.
    def visitPassTermo(self, ctx:trabalhoFinal_lucasParser.PassTermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#andOp.
    def visitAndOp(self, ctx:trabalhoFinal_lucasParser.AndOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#passTermo2.
    def visitPassTermo2(self, ctx:trabalhoFinal_lucasParser.PassTermo2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#passTermo3.
    def visitPassTermo3(self, ctx:trabalhoFinal_lucasParser.PassTermo3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#compOp.
    def visitCompOp(self, ctx:trabalhoFinal_lucasParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#equalOp.
    def visitEqualOp(self, ctx:trabalhoFinal_lucasParser.EqualOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#passTermo4.
    def visitPassTermo4(self, ctx:trabalhoFinal_lucasParser.PassTermo4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#addMinusOp.
    def visitAddMinusOp(self, ctx:trabalhoFinal_lucasParser.AddMinusOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#passTermo5.
    def visitPassTermo5(self, ctx:trabalhoFinal_lucasParser.PassTermo5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#multiDivOp.
    def visitMultiDivOp(self, ctx:trabalhoFinal_lucasParser.MultiDivOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#passTermo6.
    def visitPassTermo6(self, ctx:trabalhoFinal_lucasParser.PassTermo6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#minusUniOp.
    def visitMinusUniOp(self, ctx:trabalhoFinal_lucasParser.MinusUniOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#passTermo7.
    def visitPassTermo7(self, ctx:trabalhoFinal_lucasParser.PassTermo7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#notOp.
    def visitNotOp(self, ctx:trabalhoFinal_lucasParser.NotOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#passFator.
    def visitPassFator(self, ctx:trabalhoFinal_lucasParser.PassFatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#parenExprFat.
    def visitParenExprFat(self, ctx:trabalhoFinal_lucasParser.ParenExprFatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#idFat.
    def visitIdFat(self, ctx:trabalhoFinal_lucasParser.IdFatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#dadoFat.
    def visitDadoFat(self, ctx:trabalhoFinal_lucasParser.DadoFatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#callFuncaoFat.
    def visitCallFuncaoFat(self, ctx:trabalhoFinal_lucasParser.CallFuncaoFatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#intDado.
    def visitIntDado(self, ctx:trabalhoFinal_lucasParser.IntDadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#realDado.
    def visitRealDado(self, ctx:trabalhoFinal_lucasParser.RealDadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#stringDado.
    def visitStringDado(self, ctx:trabalhoFinal_lucasParser.StringDadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#boolDado.
    def visitBoolDado(self, ctx:trabalhoFinal_lucasParser.BoolDadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#not.
    def visitNot(self, ctx:trabalhoFinal_lucasParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#minusUni.
    def visitMinusUni(self, ctx:trabalhoFinal_lucasParser.MinusUniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#multiDiv.
    def visitMultiDiv(self, ctx:trabalhoFinal_lucasParser.MultiDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#addMinus.
    def visitAddMinus(self, ctx:trabalhoFinal_lucasParser.AddMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#equal.
    def visitEqual(self, ctx:trabalhoFinal_lucasParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#comp.
    def visitComp(self, ctx:trabalhoFinal_lucasParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#and.
    def visitAnd(self, ctx:trabalhoFinal_lucasParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#or.
    def visitOr(self, ctx:trabalhoFinal_lucasParser.OrContext):
        return self.visitChildren(ctx)



del trabalhoFinal_lucasParser