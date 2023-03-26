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


    # Visit a parse tree produced by trabalhoFinal_lucasParser#decVarConst.
    def visitDecVarConst(self, ctx:trabalhoFinal_lucasParser.DecVarConstContext):
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


    # Visit a parse tree produced by trabalhoFinal_lucasParser#decFunc.
    def visitDecFunc(self, ctx:trabalhoFinal_lucasParser.DecFuncContext):
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


    # Visit a parse tree produced by trabalhoFinal_lucasParser#print.
    def visitPrint(self, ctx:trabalhoFinal_lucasParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#input.
    def visitInput(self, ctx:trabalhoFinal_lucasParser.InputContext):
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


    # Visit a parse tree produced by trabalhoFinal_lucasParser#atribuicao.
    def visitAtribuicao(self, ctx:trabalhoFinal_lucasParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#callFunc.
    def visitCallFunc(self, ctx:trabalhoFinal_lucasParser.CallFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#expr.
    def visitExpr(self, ctx:trabalhoFinal_lucasParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#termo.
    def visitTermo(self, ctx:trabalhoFinal_lucasParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#termo2.
    def visitTermo2(self, ctx:trabalhoFinal_lucasParser.Termo2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#termo3.
    def visitTermo3(self, ctx:trabalhoFinal_lucasParser.Termo3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#termo4.
    def visitTermo4(self, ctx:trabalhoFinal_lucasParser.Termo4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#termo5.
    def visitTermo5(self, ctx:trabalhoFinal_lucasParser.Termo5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#termo6.
    def visitTermo6(self, ctx:trabalhoFinal_lucasParser.Termo6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#termo7.
    def visitTermo7(self, ctx:trabalhoFinal_lucasParser.Termo7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#fator.
    def visitFator(self, ctx:trabalhoFinal_lucasParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinal_lucasParser#dado.
    def visitDado(self, ctx:trabalhoFinal_lucasParser.DadoContext):
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