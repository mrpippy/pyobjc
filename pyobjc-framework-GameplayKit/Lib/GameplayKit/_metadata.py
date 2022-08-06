# This file is generated by objective.metadata
#
# Last update: Fri Aug  5 19:37:20 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
misc.update(
    {
        "GKBox": objc.createStructType(
            "GameplayKit.GKBox", b"{GKBox=<3f><3f>}", ["boxMin", "boxMax"]
        ),
        "GKTriangle": objc.createStructType(
            "GameplayKit.GKTriangle", b"{GKTriangle=[3<3f>]}", ["points"]
        ),
        "GKQuad": objc.createStructType(
            "GameplayKit.GKQuad", b"{GKQuad=<2f><2f>}", ["quadMin", "quadMax"]
        ),
    }
)
constants = """$$"""
enums = """$GKGameModelMaxScore@16777216$GKGameModelMinScore@-16777216$GKMeshGraphTriangulationModeCenters@2$GKMeshGraphTriangulationModeEdgeMidpoints@4$GKMeshGraphTriangulationModeVertices@1$GKRTreeSplitStrategyHalve@0$GKRTreeSplitStrategyLinear@1$GKRTreeSplitStrategyQuadratic@2$GKRTreeSplitStrategyReduceOverlap@3$"""
misc.update(
    {
        "GKMeshGraphTriangulationMode": NewType("GKMeshGraphTriangulationMode", int),
        "GKRTreeSplitStrategy": NewType("GKRTreeSplitStrategy", int),
    }
)
misc.update({})
misc.update({})
aliases = {"GK_AVAILABLE": "__OSX_AVAILABLE_STARTING"}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"GKAgent2D",
        b"position",
        {"full_signature": b"<2f>@:", "retval": {"type": b"<2f>"}},
    )
    r(
        b"GKAgent2D",
        b"setPosition:",
        {"full_signature": b"v@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(
        b"GKAgent2D",
        b"velocity",
        {"full_signature": b"<2f>@:", "retval": {"type": b"<2f>"}},
    )
    r(
        b"GKAgent3D",
        b"position",
        {"full_signature": b"<3f>@:", "retval": {"type": b"<3f>"}},
    )
    r(b"GKAgent3D", b"rightHanded", {"retval": {"type": b"Z"}})
    r(b"GKAgent3D", b"rotation", {"retval": {"type": b"{_matrix_float3x3=?}"}})
    r(
        b"GKAgent3D",
        b"setPosition:",
        {"full_signature": b"v@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(b"GKAgent3D", b"setRightHanded:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"GKAgent3D",
        b"setRotation:",
        {"arguments": {2: {"type": b"{_matrix_float3x3=?}"}}},
    )
    r(
        b"GKAgent3D",
        b"velocity",
        {"full_signature": b"<3f>@:", "retval": {"type": b"<3f>"}},
    )
    r(
        b"GKCircleObstacle",
        b"position",
        {"full_signature": b"<2f>@:", "retval": {"type": b"<2f>"}},
    )
    r(
        b"GKCircleObstacle",
        b"setPosition:",
        {"full_signature": b"v@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(b"GKDecisionTree", b"exportToURL:error:", {"retval": {"type": b"Z"}})
    r(
        b"GKGoal",
        b"goalToFollowPath:maxPredictionTime:forward:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"GKGraph",
        b"connectNodeToLowestCostNode:bidirectional:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"GKGraphNode",
        b"addConnectionsToNodes:bidirectional:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"GKGraphNode",
        b"removeConnectionsToNodes:bidirectional:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"GKGraphNode2D",
        b"initWithPoint:",
        {"full_signature": b"@@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(
        b"GKGraphNode2D",
        b"nodeWithPoint:",
        {"full_signature": b"@@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(
        b"GKGraphNode2D",
        b"position",
        {"full_signature": b"<2f>@:", "retval": {"type": b"<2f>"}},
    )
    r(
        b"GKGraphNode2D",
        b"setPosition:",
        {"full_signature": b"v@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(
        b"GKGraphNode3D",
        b"initWithPoint:",
        {"full_signature": b"@@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(
        b"GKGraphNode3D",
        b"nodeWithPoint:",
        {"full_signature": b"@@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(
        b"GKGraphNode3D",
        b"position",
        {"full_signature": b"<3f>@:", "retval": {"type": b"<3f>"}},
    )
    r(
        b"GKGraphNode3D",
        b"setPosition:",
        {"full_signature": b"v@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(b"GKGridGraph", b"diagonalsAllowed", {"retval": {"type": b"Z"}})
    r(
        b"GKGridGraph",
        b"graphFromGridStartingAt:width:height:diagonalsAllowed:",
        {
            "full_signature": b"@@:<2i>iiZ",
            "arguments": {2: {"type": b"<2i>"}, 5: {"type": b"Z"}},
        },
    )
    r(
        b"GKGridGraph",
        b"graphFromGridStartingAt:width:height:diagonalsAllowed:nodeClass:",
        {
            "full_signature": b"@@:<2i>iiZ#",
            "arguments": {2: {"type": b"<2i>"}, 5: {"type": b"Z"}},
        },
    )
    r(
        b"GKGridGraph",
        b"gridOrigin",
        {"full_signature": b"<2i>@:", "retval": {"type": b"<2i>"}},
    )
    r(
        b"GKGridGraph",
        b"initFromGridStartingAt:width:height:diagonalsAllowed:",
        {
            "full_signature": b"@@:<2i>iiZ",
            "arguments": {2: {"type": b"<2i>"}, 5: {"type": b"Z"}},
        },
    )
    r(
        b"GKGridGraph",
        b"initFromGridStartingAt:width:height:diagonalsAllowed:nodeClass:",
        {
            "full_signature": b"@@:<2i>iiZ#",
            "arguments": {2: {"type": b"<2i>"}, 5: {"type": b"Z"}},
        },
    )
    r(
        b"GKGridGraph",
        b"nodeAtGridPosition:",
        {"full_signature": b"@@:<2i>", "arguments": {2: {"type": b"<2i>"}}},
    )
    r(
        b"GKGridGraphNode",
        b"gridPosition",
        {"full_signature": b"<2i>@:", "retval": {"type": b"<2i>"}},
    )
    r(
        b"GKGridGraphNode",
        b"initWithGridPosition:",
        {"full_signature": b"@@:<2i>", "arguments": {2: {"type": b"<2i>"}}},
    )
    r(
        b"GKGridGraphNode",
        b"nodeWithGridPosition:",
        {"full_signature": b"@@:<2i>", "arguments": {2: {"type": b"<2i>"}}},
    )
    r(
        b"GKMeshGraph",
        b"graphWithBufferRadius:minCoordinate:maxCoordinate:",
        {
            "full_signature": b"@@:f<2f><2f>",
            "arguments": {3: {"type": b"<2f>"}, 4: {"type": b"<2f>"}},
        },
    )
    r(
        b"GKMeshGraph",
        b"graphWithBufferRadius:minCoordinate:maxCoordinate:nodeClass:",
        {
            "full_signature": b"@@:f<2f><2f>#",
            "arguments": {3: {"type": b"<2f>"}, 4: {"type": b"<2f>"}},
        },
    )
    r(
        b"GKMeshGraph",
        b"initWithBufferRadius:minCoordinate:maxCoordinate:",
        {
            "full_signature": b"@@:f<2f><2f>",
            "arguments": {3: {"type": b"<2f>"}, 4: {"type": b"<2f>"}},
        },
    )
    r(
        b"GKMeshGraph",
        b"initWithBufferRadius:minCoordinate:maxCoordinate:nodeClass:",
        {
            "full_signature": b"@@:f<2f><2f>#",
            "arguments": {3: {"type": b"<2f>"}, 4: {"type": b"<2f>"}},
        },
    )
    r(
        b"GKMeshGraph",
        b"triangleAtIndex:",
        {"retval": {"type": b"{GKTriangle=[3<3f>]}"}},
    )
    r(b"GKNSPredicateRule", b"evaluatePredicateWithSystem:", {"retval": {"type": b"Z"}})
    r(
        b"GKNoise",
        b"moveBy:",
        {"full_signature": b"v@:<3d>", "arguments": {2: {"type": b"<3d>"}}},
    )
    r(
        b"GKNoise",
        b"remapValuesToTerracesWithPeaks:terracesInverted:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"GKNoise",
        b"rotateBy:",
        {"full_signature": b"v@:<3d>", "arguments": {2: {"type": b"<3d>"}}},
    )
    r(
        b"GKNoise",
        b"scaleBy:",
        {"full_signature": b"v@:<3d>", "arguments": {2: {"type": b"<3d>"}}},
    )
    r(
        b"GKNoise",
        b"valueAtPosition:",
        {"full_signature": b"f@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(
        b"GKNoiseMap",
        b"initWithNoise:size:origin:sampleCount:seamless:",
        {
            "full_signature": b"@@:@<2d><2d><2i>Z",
            "arguments": {
                3: {"type": b"<2d>"},
                4: {"type": b"<2d>"},
                5: {"type": b"<2i>"},
                6: {"type": b"Z"},
            },
        },
    )
    r(
        b"GKNoiseMap",
        b"interpolatedValueAtPosition:",
        {"full_signature": b"f@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(b"GKNoiseMap", b"isSeamless", {"retval": {"type": b"Z"}})
    r(
        b"GKNoiseMap",
        b"noiseMapWithNoise:size:origin:sampleCount:seamless:",
        {
            "full_signature": b"@@:@<2d><2d><2i>Z",
            "arguments": {
                3: {"type": b"<2d>"},
                4: {"type": b"<2d>"},
                5: {"type": b"<2i>"},
                6: {"type": b"Z"},
            },
        },
    )
    r(
        b"GKNoiseMap",
        b"origin",
        {"full_signature": b"<2d>@:", "retval": {"type": b"<2d>"}},
    )
    r(
        b"GKNoiseMap",
        b"sampleCount",
        {"full_signature": b"<2i>@:", "retval": {"type": b"<2i>"}},
    )
    r(
        b"GKNoiseMap",
        b"setValue:atPosition:",
        {"full_signature": b"v@:f<2i>", "arguments": {3: {"type": b"<2i>"}}},
    )
    r(
        b"GKNoiseMap",
        b"size",
        {"full_signature": b"<2d>@:", "retval": {"type": b"<2d>"}},
    )
    r(
        b"GKNoiseMap",
        b"valueAtPosition:",
        {"full_signature": b"f@:<2i>", "arguments": {2: {"type": b"<2i>"}}},
    )
    r(
        b"GKObstacleGraph",
        b"isConnectionLockedFromNode:toNode:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"GKOctree",
        b"addElement:withBox:",
        {"arguments": {3: {"type": b"{GKBox=<3f><3f>}"}}},
    )
    r(
        b"GKOctree",
        b"addElement:withPoint:",
        {"full_signature": b"@@:@<3f>", "arguments": {3: {"type": b"<3f>"}}},
    )
    r(
        b"GKOctree",
        b"elementsAtPoint:",
        {"full_signature": b"@@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(b"GKOctree", b"elementsInBox:", {"arguments": {2: {"type": b"{GKBox=<3f><3f>}"}}})
    r(
        b"GKOctree",
        b"initWithBoundingBox:minimumCellSize:",
        {"arguments": {2: {"type": b"{GKBox=<3f><3f>}"}}},
    )
    r(
        b"GKOctree",
        b"octreeWithBoundingBox:minimumCellSize:",
        {"arguments": {2: {"type": b"{GKBox=<3f><3f>}"}}},
    )
    r(b"GKOctree", b"removeElement:", {"retval": {"type": b"Z"}})
    r(b"GKOctree", b"removeElement:withNode:", {"retval": {"type": b"Z"}})
    r(b"GKOctreeNode", b"box", {"retval": {"type": b"{GKBox=<3f><3f>}"}})
    r(
        b"GKPath",
        b"float2AtIndex:",
        {"full_signature": b"<2f>@:Q", "retval": {"type": b"<2f>"}},
    )
    r(
        b"GKPath",
        b"float3AtIndex:",
        {"full_signature": b"<3f>@:Q", "retval": {"type": b"<3f>"}},
    )
    r(
        b"GKPath",
        b"initWithFloat3Points:count:radius:cyclical:",
        {"arguments": {2: {"arg_size_in_arg": 1, "type": "n"}, 5: {"type": b"Z"}}},
    )
    r(
        b"GKPath",
        b"initWithPoints:count:radius:cyclical:",
        {"arguments": {2: {"arg_size_in_arg": 1, "type": "n"}, 5: {"type": b"Z"}}},
    )
    r(b"GKPath", b"isCyclical", {"retval": {"type": b"Z"}})
    r(
        b"GKPath",
        b"pathWithFloat3Points:count:radius:cyclical:",
        {"arguments": {2: {"arg_size_in_arg": 1, "type": "n"}, 5: {"type": b"Z"}}},
    )
    r(
        b"GKPath",
        b"pathWithPoints:count:radius:cyclical:",
        {"arguments": {2: {"arg_size_in_arg": 1, "type": "n"}, 5: {"type": b"Z"}}},
    )
    r(
        b"GKPath",
        b"pointAtIndex:",
        {"deprecated": 1012, "full_signature": b"<2f>@:Q", "retval": {"type": b"<2f>"}},
    )
    r(b"GKPath", b"setCyclical:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"GKPolygonObstacle",
        b"initWithPoints:count:",
        {"arguments": {2: {"arg_size_in_arg": 1, "type": "n"}}},
    )
    r(
        b"GKPolygonObstacle",
        b"obstacleWithPoints:count:",
        {"arguments": {2: {"arg_size_in_arg": 1, "type": "n"}}},
    )
    r(
        b"GKPolygonObstacle",
        b"vertexAtIndex:",
        {"full_signature": b"<2f>@:Q", "retval": {"type": b"<2f>"}},
    )
    r(
        b"GKQuadtree",
        b"addElement:withPoint:",
        {"full_signature": b"@@:@<2f>", "arguments": {3: {"type": b"<2f>"}}},
    )
    r(
        b"GKQuadtree",
        b"addElement:withQuad:",
        {"arguments": {3: {"type": b"{GKQuad=<2f><2f>}"}}},
    )
    r(
        b"GKQuadtree",
        b"elementsAtPoint:",
        {"full_signature": b"@@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(
        b"GKQuadtree",
        b"elementsInQuad:",
        {"arguments": {2: {"type": b"{GKQuad=<2f><2f>}"}}},
    )
    r(
        b"GKQuadtree",
        b"initWithBoundingQuad:minimumCellSize:",
        {"arguments": {2: {"type": b"{GKQuad=<2f><2f>}"}}},
    )
    r(
        b"GKQuadtree",
        b"quadtreeWithBoundingQuad:minimumCellSize:",
        {"arguments": {2: {"type": b"{GKQuad=<2f><2f>}"}}},
    )
    r(b"GKQuadtree", b"removeElement:", {"retval": {"type": b"Z"}})
    r(b"GKQuadtree", b"removeElement:withNode:", {"retval": {"type": b"Z"}})
    r(b"GKQuadtreeNode", b"quad", {"retval": {"type": b"{GKQuad=<2f><2f>}"}})
    r(
        b"GKRTree",
        b"addElement:boundingRectMin:boundingRectMax:splitStrategy:",
        {
            "full_signature": b"v@:@<2f><2f>q",
            "arguments": {3: {"type": b"<2f>"}, 4: {"type": b"<2f>"}},
        },
    )
    r(
        b"GKRTree",
        b"elementsInBoundingRectMin:rectMax:",
        {
            "full_signature": b"@@:<2f><2f>",
            "arguments": {2: {"type": b"<2f>"}, 3: {"type": b"<2f>"}},
        },
    )
    r(
        b"GKRTree",
        b"removeElement:boundingRectMin:boundingRectMax:",
        {
            "full_signature": b"v@:@<2f><2f>",
            "arguments": {3: {"type": b"<2f>"}, 4: {"type": b"<2f>"}},
        },
    )
    r(b"GKRandomDistribution", b"nextBool", {"retval": {"type": b"Z"}})
    r(b"GKRule", b"evaluatePredicateWithSystem:", {"retval": {"type": b"Z"}})
    r(
        b"GKRule",
        b"ruleWithBlockPredicate:action:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
            }
        },
    )
    r(
        b"GKSphereObstacle",
        b"position",
        {"full_signature": b"<3f>@:", "retval": {"type": b"<3f>"}},
    )
    r(
        b"GKSphereObstacle",
        b"setPosition:",
        {"full_signature": b"v@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(b"GKState", b"isValidNextState:", {"retval": {"type": b"Z"}})
    r(b"GKStateMachine", b"canEnterState:", {"retval": {"type": b"Z"}})
    r(b"GKStateMachine", b"enterState:", {"retval": {"type": b"Z"}})
    r(
        b"GKVoronoiNoiseSource",
        b"initWithFrequency:displacement:distanceEnabled:seed:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"GKVoronoiNoiseSource", b"isDistanceEnabled", {"retval": {"type": b"Z"}})
    r(
        b"GKVoronoiNoiseSource",
        b"setDistanceEnabled:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"GKVoronoiNoiseSource",
        b"voronoiNoiseWithFrequency:displacement:distanceEnabled:seed:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"NSObject", b"activePlayer", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"agentDidUpdate:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"agentWillUpdate:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"applyGameModelUpdate:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"bestMoveForActivePlayer",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(b"NSObject", b"gameModel", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"gameModelUpdatesForPlayer:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"isLossForPlayer:",
        {"required": False, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"isWinForPlayer:",
        {"required": False, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"nextBool", {"required": True, "retval": {"type": b"Z"}})
    r(b"NSObject", b"nextInt", {"required": True, "retval": {"type": b"q"}})
    r(
        b"NSObject",
        b"nextIntWithUpperBound:",
        {"required": True, "retval": {"type": b"Q"}, "arguments": {2: {"type": b"Q"}}},
    )
    r(b"NSObject", b"nextUniform", {"required": True, "retval": {"type": b"f"}})
    r(
        b"NSObject",
        b"playerId",
        {"required": True, "retval": {"type": sel32or64(b"i", b"q")}},
    )
    r(b"NSObject", b"players", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"randomSource", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"scoreForPlayer:",
        {"required": False, "retval": {"type": b"q"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setGameModel:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"setPlayerId:", {"arguments": {2: {"type": sel32or64(b"i", b"q")}}})
    r(
        b"NSObject",
        b"setRandomSource:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setValue:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"q"}}},
    )
    r(
        b"NSObject",
        b"unapplyGameModelUpdate:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"value", {"required": True, "retval": {"type": b"q"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
