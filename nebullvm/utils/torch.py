from typing import List, Tuple

import torch
from torch.nn import Module

from nebullvm.base import DataType, InputInfo


def get_outputs_sizes_torch(
    torch_model: Module, input_tensors: List[torch.Tensor]
) -> List[Tuple[int, ...]]:
    if torch.cuda.is_available():
        input_tensors = [x.cuda() for x in input_tensors]
        torch_model.cuda()
    with torch.no_grad():
        outputs = torch_model(*input_tensors)
        if isinstance(outputs, torch.Tensor):
            return [tuple(outputs.size())[1:]]
        else:
            return [tuple(output.size())[1:] for output in outputs]


def create_model_inputs_torch(
    batch_size: int, input_infos: List[InputInfo]
) -> List[torch.Tensor]:
    input_tensors = (
        torch.randn((batch_size, *input_info.size))
        if input_info.dtype is DataType.FLOAT
        else torch.randint(
            size=(batch_size, *input_info.size),
            low=input_info.min_value or 0,
            high=input_info.max_value or 100,
        )
        for input_info in input_infos
    )
    return list(input_tensors)
