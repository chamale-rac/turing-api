from .utils.constants import displacementReplacements


class Transition:
    def __init__(self, initialState: str,
                 initialMemCacheValue: str,
                 tapeInput: str,
                 finalState: str,
                 finalMemCacheValue: str,
                 tapeOutput: str,
                 tapeDisplacement: int) -> None:
        self.initialState: str = initialState
        self.initialMemCacheValue: str = initialMemCacheValue
        self.tapeInput: str = tapeInput
        self.finalState: str = finalState
        self.finalMemCacheValue: str = finalMemCacheValue
        self.tapeOutput: str = tapeOutput
        self.tapeDisplacement: int = displacementReplacements[tapeDisplacement]

    def __eq__(self, __value: object) -> bool:
        '''
        Args: 
            __value (object): The value to compare against

        Can be compared against tuples of the form (initialState, tapeInput, memCacheValue) or other Transition objects (completeness)
        '''
        if isinstance(__value, tuple):
            if len(__value) == 3:
                return self.initialState == __value[0] and self.initialMemCacheValue == __value[1] and self.tapeInput == __value[2]
            elif len(__value) == 2:
                return self.initialState == __value[0] and self.tapeInput == __value[1]
        return False

    def __str__(self) -> str:
        tapeDisplacement = displacementReplacements[self.tapeDisplacement]
        return f'[{self.initialState}, {self.initialMemCacheValue}], {self.tapeInput} = [{self.finalState}, {self.finalMemCacheValue}], {self.tapeOutput}, {tapeDisplacement}'
