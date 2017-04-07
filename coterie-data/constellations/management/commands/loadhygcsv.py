import csv
import pprint

from django.core.management.base import BaseCommand, CommandError
from constellations.models import Constellation, Star

class Command(BaseCommand):
    help = 'Load the HYG database csv.'
    _hyg_translation = [('absmag', 'abs_magnitude'),
                        ('base', 'multi_star_hyg_id'),
                        ('bayer', 'bayer'),
                        ('bf', 'bayer_flamsteed_designation'),
                        ('ci', 'color_index'),
                        ('comp', 'companion_star_hyg_id'),
                        ('comp_primary', 'companion_primary_star_hyg_id'),
                        ('con', 'constellation_abbreviation'),
                        ('dec', 'declination'),
                        ('decrad', 'declination_rad'),
                        ('dist', 'distance_pc'),
                        ('flam', 'flamsteed_number'),
                        ('gl', 'gliese_id'),
                        ('hd', 'henry_draper_id'),
                        ('id', 'hyg_id'),
                        ('lum', 'luminosity'),  # sols
                        ('mag', 'magnitude'),  # apparent
                        ('pmdec', 'proper_motion_declination'),  # millisec/yr
                        ('pmdecrad', 'proper_motion_declination_rad'),
                        ('pmra', 'proper_motion_right_ascention'),
                        ('pmrarad', 'proper_motion_right_ascention_rad'),
                        ('proper', 'proper_name'),
                        ('ra', 'right_ascention'),
                        ('rarad', 'right_ascention_rad'),
                        ('rv', 'radial_velocity'),  # km/s
                        ('spect', 'spectral_type'),
                        ('var', 'variable_star_designation'),
                        ('var_max', 'variable_max_magnitude'),  # approx magnitude
                        ('var_min', 'variable_min_magnitude'),
                        ('vx', 'velocity_x'),
                        ('vy', 'velocity_y'),
                        ('vz', 'velocity_z'),
                        ('x', 'x'),
                        ('y', 'y'),
                        ('z', 'z')]

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='?')
        parser.add_argument('--reset', action='store_true', default=False)

    def handle(self, *args, **options):
        if self._data_exists():
            if not options['reset']:
                raise CommandError('Star and Constellation data exist, use --reset to delete it before loading HYG csv')
            else:
                self._reset_data()

        self._load_constellations(options)

    def _load_constellations(self, options):
        constellations = {}
        with open(options['csv_file']) as star_fh:
            star_reader = csv.DictReader(star_fh)
            for star in star_reader:
                if star['con'] and star['con'] not in constellations:
                    constellations[star['con']] = None

        Constellation.objects.bulk_create([Constellation(abbreviation=x)
                                          for x in constellations.keys()])

        stars = []
        with open(options['csv_file']) as star_fh:
            star_reader = csv.DictReader(star_fh)
            for star in star_reader:
                star_data = {}
                if star['con']:
                    if constellations[star['con']] is None:
                        constellations[star['con']] = Constellation.objects.get(abbreviation=star['con']).pk
                    star_data['constellation_id'] = constellations[star['con']]
                for label in self._hyg_translation:
                    if star[label[0]]:
                        star_data[label[1]] = star[label[0]]
                stars.append(star_data)
        pprint.pprint(constellations)

        Star.objects.bulk_create([Star(**x) for x in stars])

        # XXX must deal with foreign key

    def _data_exists(self):
        return (Constellation.objects.count() + Star.objects.count()) > 0

    def _reset_data(self):
        Constellation.objects.all().delete()
        Star.objects.all().delete()
