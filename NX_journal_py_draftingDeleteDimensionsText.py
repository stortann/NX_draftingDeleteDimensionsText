# NX 2412
# Delete all of the dimensions' text on every sheet

import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Drafting
import NXOpen.Drawings
import NXOpen.MenuBar


def main():

    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    for myDimension in workPart.Dimensions:

        objects1 = [NXOpen.DisplayableObject.Null] * 1
        objects1[0] = myDimension
        editSettingsBuilder1 = (
            workPart.SettingsManager.CreateAnnotationEditSettingsBuilder(objects1)
        )

        editSettingsBuilder1.AnnotationStyle.DimensionStyle.OverrideDimensionText = True

        customizedtext1 = [""]
        editSettingsBuilder1.AnnotationStyle.DimensionStyle.SetOverriddenDimensionText(
            customizedtext1
        )

        nXObject1 = editSettingsBuilder1.Commit()
        editSettingsBuilder1.Destroy()


if __name__ == "__main__":
    main()
