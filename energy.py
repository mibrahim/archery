#!/usr/bin/python

weightLbs = 67.6 * 0.75
weightKgs = weightLbs * 0.453592
weightPullInches = 28
weightPullMeters = weightPullInches * 0.0254

bowSaddleInches = 6.25
bowSaddleMeters = bowSaddleInches * 0.0254

k = 9.81 * weightKgs / ( weightPullMeters - bowSaddleMeters )

print "weightPull = ", weightPullMeters

print "k = ",k

drawInches = 28
drawMeters = drawInches * 0.0254

print "draw = ", drawMeters

energyJoules = 0.5 * k * (( drawMeters - bowSaddleMeters) ** 2)
energyFtLbs = energyJoules * 0.737562

print "Energy @",drawInches," = ",energyFtLbs," ft.lbs"

bowEfficiency = 0.8

arrowGrains = 380
arrowKg = arrowGrains * 0.0647989 / 1000

kineticEnergy = bowEfficiency * energyJoules

arrowVelocity = (2 * kineticEnergy / arrowKg ) ** 0.5

arrowFPS = 3.28084 * arrowVelocity

print "Arrow speed = ", arrowFPS, " fps"
