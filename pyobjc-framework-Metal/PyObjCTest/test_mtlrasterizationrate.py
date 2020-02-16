from PyObjCTools.TestSupport import *

import Metal

class TestMTLRasterizationRateHelper(Metal.NSObject):
    def screenSize(self): return 1
    def physicalGranularity(self): return 1
    def layerCount(self): return 1
    def parameterBufferSizeAndAlign(self): return 1
    def copyParameterDataToBuffer_offset_(self, a, b): pass
    def physicalSizeForLayer_(self, a): return 1
    def mapScreenToPhysicalCoordinates_forLayer_(self, a): return 1
    def mapPhysicalToScreenCoordinates_forLayer_(self, a): return 1

class TestMTLRasterizationRate(TestCase):

    def test_methods(self):
        self.assertResultHasType(TestMTLRasterizationRateHelper.screenSize, Metal.MTLSize.__typestr__)
        self.assertResultHasType(TestMTLRasterizationRateHelper.physicalGranularity, Metal.MTLSize.__typestr__)
        self.assertResultHasType(TestMTLRasterizationRateHelper.layerCount, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLRasterizationRateHelper.parameterBufferSizeAndAlign, Metal.MTLSizeAndAlign.__typestr__)
        self.assertArgHasType(TestMTLRasterizationRateHelper.copyParameterDataToBuffer_offset_, 1, objc._C_NSUInteger)

        self.assertResultHasType(TestMTLRasterizationRateHelper.physicalSizeForLayer_, Metal.MTLSize.__typestr__)
        self.assertArgHasType(TestMTLRasterizationRateHelper.physicalSizeForLayer_, 0, objc._C_NSUInteger)

        self.assertResultHasType(TestMTLRasterizationRateHelper.mapScreenToPhysicalCoordinates_forLayer_, Metal.MTLCoordinate2D.__typestr__)
        self.assertArgHasType(TestMTLRasterizationRateHelper.mapScreenToPhysicalCoordinates_forLayter_, 0, Metal.MTLCoordinate2D.__typestr__)
        self.assertArgHasType(TestMTLRasterizationRateHelper.mapScreenToPhysicalCoordinates_forLayter_, 1, objc._C_NSUInteger)

        self.assertResultHasType(TestMTLRasterizationRateHelper.mapPhysicalToScreenCoordinates_forLayer_, Metal.MTLCoordinate2D.__typestr__)
        self.assertArgHasType(TestMTLRasterizationRateHelper.mapPhysicalToScreenCoordinates_forLayter_, 0, Metal.MTLCoordinate2D.__typestr__)
        self.assertArgHasType(TestMTLRasterizationRateHelper.mapPhysicalToScreenCoordinates_forLayter_, 1, objc._C_NSUInteger)

    @min_os_level("10.15.4")
    def test_methods10_15_4(self):
        self.assertArgIsIn(
            Metal.MTLRasterizationRateLayerDescriptor.initWithSampleCount_horizontal_vertical_, 1)
        )
        self.assertArgSizeInArg(
            Metal.MTLRasterizationRateLayerDescriptor.initWithSampleCount_horizontal_vertical_, 1, 0)
        )
        self.assertArgIsIn(
            Metal.MTLRasterizationRateLayerDescriptor.initWithSampleCount_horizontal_vertical_, 2)
        )
        self.assertArgSizeInArg(
            Metal.MTLRasterizationRateLayerDescriptor.initWithSampleCount_horizontal_vertical_, 2, 0)
        )

        # XXX: Mutable buffer
        self.assertResultIsVariableSize(
                Metal.MTLRasterizationRateLayerDescriptor.horizontalSampleStorage)
        self.assertResultIsVariableSize(
                Metal.MTLRasterizationRateLayerDescriptor.verticalSampleStorage)


        self.assertArgIsIn(Metal.MTLRasterizationRateMapDescriptor.rasterizationRateMapDescriptorWithScreenSize_layerCount_layers_, 2)
        self.assertArgSizeInArg(Metal.MTLRasterizationRateMapDescriptor.rasterizationRateMapDescriptorWithScreenSize_layerCount_layers_, 2, 1)

    @min_sdk_level('10.15')
    def test_protocols(self):
        objc.protocolNamed('MTLRasterizationRateMap')

