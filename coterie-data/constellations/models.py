from django.db import models

# Create your models here.


class Constellation(models.Model):
    abbreviation = models.CharField(max_length=256)

    def __str__(self):
        return self.abbreviation


class Star(models.Model):
    '''
    A full mapping of values in the HYG database,
    columns renamed to english words.
    '''
    constellation = models.ForeignKey('Constellation', null=True, blank=True)
    abs_magnitude = models.DecimalField(max_digits=6, decimal_places=4, blank=False, null=False)
    multi_star_hyg_id = models.CharField(max_length=8, null=True, blank=True)
    bayer = models.CharField(max_length=8, blank=True, null=False, default="")
    bayer_flamsteed_designation = models.CharField(max_length=12, blank=True, null=False, default="")
    color_index = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    companion_star_hyg_id = models.PositiveIntegerField(null=True, blank=True)
    companion_primary_star_hyg_id = models.PositiveIntegerField(null=True, blank=True)
    constellation_abbreviation = models.CharField(max_length=3, blank=True, null=False, default="")
    declination = models.DecimalField(max_digits=8, decimal_places=6, blank=False)
    declination_rad = models.DecimalField(max_digits=16, decimal_places=15, blank=False)
    distance_pc = models.DecimalField(max_digits=10, decimal_places=4, blank=False, null=False)
    flamsteed_number = models.CharField(max_length=3, blank=True, null=False, default="")
    gliese_id = models.CharField(max_length=9, blank=True, null=False, default="")
    henry_draper_id = models.CharField(max_length=6, blank=True, null=False, default="")
    hyg_id = models.PositiveIntegerField(null=True, blank=True)
    luminosity = models.FloatField()
    magnitude = models.DecimalField(max_digits=4, decimal_places=2)
    proper_motion_declination = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    proper_motion_declination_rad = models.FloatField(null=True, )
    proper_motion_right_ascention = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    proper_motion_right_ascention_rad = models.FloatField(null=True)
    proper_name = models.CharField(max_length=24, blank=True, null=False, default="")
    right_ascention = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    right_ascention_rad = models.FloatField()
    radial_velocity = models.DecimalField(max_digits=4, decimal_places=1, blank=True)
    spectral_type = models.CharField(max_length=12, blank=True, null=False, default="")
    variable_star_designation = models.CharField(max_length=5, blank=True, null=False, default="")
    variable_max_magnitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    variable_min_magnitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    velocity_x = models.DecimalField(max_digits=12, decimal_places=8, blank=False, null=False)
    velocity_y = models.DecimalField(max_digits=12, decimal_places=8, blank=False, null=False)
    velocity_z = models.DecimalField(max_digits=12, decimal_places=8, blank=False, null=False)
    x = models.DecimalField(max_digits=12, decimal_places=6, blank=False, null=False)
    y = models.DecimalField(max_digits=12, decimal_places=6, blank=False, null=False)
    z = models.DecimalField(max_digits=12, decimal_places=6, blank=False, null=False)

    def get_name(self):
        if self.proper_name:
            return self.proper_name
        if self.bayer_flamsteed_designation:
            return self.bayer_flamsteed_designation
        return str(self.hyg_id)

    def __str__(self):
        return self.get_name()
