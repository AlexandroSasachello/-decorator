class AbstractBlock:
    """ Абстрактный блок
    """

    def draw(self):
        raise NotImplementedError();


class TerminatorBlock(AbstractBlock):
    """ Терминальный блок (начало/конец, вход/выход)
    """

    def draw(self):
        print("Terminator block drawing ... ")


class ProcessBlock(AbstractBlock):
    """ Блок - процесс (один или несколько операторов)
    """

    def draw(self):
        print("Process block drawing ... ")


class AbstractBlockDecorator(AbstractBlock):
    """ Абстракный декоратор блоков
    """

    def __init__(self, decoratee):
        # _decoratee - ссылка на декорируемый объект
        self._decoratee = decoratee

    def draw(self):
        self._decoratee.draw()


class LabelBlockDecorator(AbstractBlockDecorator):
    """ Декорирует блок текстовой меткой
    """

    def __init__(self, decoratee, label):
        self._decoratee = decoratee
        self._label = label

    def draw(self):
        AbstractBlockDecorator.draw(self)
        self._drawLabel()

    def _drawLabel(self):
        print(" ... drawing label " + self._label)


class BorderBlockDecorator(AbstractBlockDecorator):
    """ Декорирует блок специальной рамкой
    """

    def __init__(self, decoratee, borderWidth):
        self._decoratee = decoratee
        self._borderWidth = borderWidth

    def draw(self):
        AbstractBlockDecorator.draw(self)
        self._drawBorder()

    def _drawBorder(self):
        print(" ... drawing border with width " + str(self._borderWidth))


# терминальный блок
tBlock = TerminatorBlock()
# блок - процесс
pBlock = ProcessBlock()

# Применим LabelDecorator к терминальному блоку
labelDecorator = LabelBlockDecorator(tBlock, "Label222")

# Применим BorderDecorator к терминальному блоку, после применения LabelDecorator
borderDecorator1 = BorderBlockDecorator(labelDecorator, 22)

# Применим BorderDecorator к блоку - процессу
borderDecorator2 = BorderBlockDecorator(pBlock, 22)

labelDecorator.draw()
borderDecorator1.draw()
borderDecorator2.draw()