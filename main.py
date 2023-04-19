from typing import List, Dict, Union

list_1: List[
    Dict[
        str | int | object,
        str | int
    ]
] = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2: List[
    Dict[
        str | int | object,
        Union[str, int, Dict[str, str | int]]
    ]
] = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(
    list_1: List[
        Dict[
            str | int | object,
            str | int | object
        ]
    ],
    list_2: List[
        Dict[
            str | int | object,
            str | int | object
        ]
    ]
) -> List[
    Dict[
        str | int | object,
        str | int | object
    ]
]:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    # return list_3

    map_1: Dict[
        str | int | object,
        Dict[str | int | object, str | int | object]
    ] = {
        dict1["id"]: dict1 for dict1 in list_1
    }

    map_2: Dict[
        str | int | object,
        Dict[str | int | object, str | int | object]
    ] = {
        dict2["id"]: dict2 for dict2 in list_2
    }

    list_3: List[
        Dict[
            str | int | object,
            str | int | object
        ]
    ] = []

    for id in map_1.keys():
        try:
            list_3.append(map_1[id] | map_2[id])
        except KeyError:
            list_3.append(map_1[id])

    print(list_3)
    return list_3


list_3: List[
    Dict[
        str | int | object,
        str | int | object
    ]
] = merge_lists(list_1, list_2)
